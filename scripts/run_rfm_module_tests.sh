#!/bin/bash

# This script runs ALL Reframe module tests, with no exceptions

if [ -n "${PAWSEY_CLUSTER}" ] && [ -z ${SYSTEM+x} ]; then
    SYSTEM="$PAWSEY_CLUSTER"
fi

if [ -z ${SYSTEM+x} ]; then
    echo "The 'SYSTEM' variable is not set. Please specify the system you want to
    build Spack for."
    exit 1
fi

# Set to repo of deployed stack (otherwise hashes of some packages may not match)
# This should most often be the repo where this script is located
PAWSEY_SPACK_CONFIG_REPO=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/.." &> /dev/null && pwd )
. "${PAWSEY_SPACK_CONFIG_REPO}/systems/${SYSTEM}/settings.sh"

# Needed while 2023.08 stack is concurrent with 2024.05 due to ansys-fluids/2022R1
# Can be removed/commented out after 2023.08 stack is gone
# Comment this line if running tests over 2023.08 stack
module unuse /software/setonix/2023.08/modules/zen3/gcc/12.2.0/applications

# Use the modules from the new stack
module use ${INSTALL_PREFIX}/staff_modulefiles
module --ignore-cache load pawseyenv/${pawseyenv_version}
# swap is needed for the pawsey_temp module to work
module swap PrgEnv-gnu PrgEnv-cray
module swap PrgEnv-cray PrgEnv-gnu

# These need to be exported to be accessible within Reframe tests
export PAWSEY_SPACK_CONFIG_REPO=${PAWSEY_SPACK_CONFIG_REPO}
export cce_version=${cce_version}
export gcc_version=${gcc_version}
export python_version=${python_version}
export reframe_version=3.12.0


# If running on compute node, add node this job is running on to host list of ReFrame, allowing it to run from this node
hn=$(hostname)
if [[ $hn == *"nid"* ]]; then
    sed -i "s/\(hostnames.*setonix-01.*\).*\(\]\)/\1,'${SLURM_JOB_NODELIST}'\2/" ${RFM_SETTINGS_FILE}
fi

# Reframe testing for modules
module load reframe/${reframe_version}
#module load reframe/3.12.0
# Add rocm environment to environment list for testing
# Can't be added to setting.sh since spack tries to install those packages straightaway
env_list+="rocm"
for env in $env_list; do
  echo "Running ReFrame tests for modules in env $env"
  export SPACK_ENV=${env}
  reframe -C ${RFM_SETTINGS_FILE} -c ${RFM_TEST_FILE} --prefix=${RFM_STORAGE_DIR} --report-file=${RFM_STORAGE_DIR}/rfm_install_report_${env}.json -t installation -r
  unset SPACK_ENV
  mv reframe.out ${RFM_STORAGE_DIR}/reframe_${env}_install.out
  mv reframe.log ${RFM_STORAGE_DIR}/reframe_${env}_install.log
done

for env in $cray_env_list; do
  echo "Running ReFrame tests for modules in env $env"
  export SPACK_ENV=${env}
  reframe -C ${RFM_SETTINGS_FILE} -c ${RFM_TEST_FILE} --prefix=${RFM_STORAGE_DIR} --report-file=${RFM_STORAGE_DIR}/rfm_install_report_${env}.json -t installation -r
  unset SPACK_ENV
  mv reframe.out ${RFM_STORAGE_DIR}/reframe_${env}_install.out
  mv reframe.log ${RFM_STORAGE_DIR}/reframe_${env}_install.log
done

# Reset valid setonix hostnames to original entries (i.e. remove the node this job runs on) for future runs
if [[ $hn == *"nid"* ]]; then
    sed -i "s/\(hostnames.*setonix-01.*\)\(,.*\]\)/\1]/" ${RFM_SETTINGS_FILE}
fi
