# Copyright 2016-2022 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause


#
# This file was automatically generated by ReFrame based on 'setup_files/settings.py'.  # noqa: E501
# Most of this file taken from Deva's settings.py file in reframe/setup_files/ on bitbucket
#

site_configuration = {
    'systems': [
        {
            'name': 'setonix',
            'descr': 'Setonix',
            'hostnames': ['setonix-01', 'setonix-02', 'setonix-03','setonix-04','setonix-09'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'login',
                    'descr': 'Setonix login node',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'modules': [],
                    'access': [],
                    'max_jobs': 1,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },
                {
                    'name': 'work',
                    'descr': 'Setonix work (compute nodes) partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=work'],
                    'max_jobs': 32,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },
                {
                    'name': 'askaprt',
                    'descr': 'Setonix askaprt (compute nodes) partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=askaprt'],
                    'max_jobs': 32,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },                
                {
                    'name': 'copy',
                    'descr': 'Setonix copy (data mover) nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=copy'],
                    'max_jobs': 1,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                },
                {
                    'name': 'debug',
                    'descr': 'Setonix debug partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=debug'],
                    'max_jobs': 1,
                    'environs': ['PrgEnv-aocc', 'PrgEnv-cray', 'PrgEnv-gnu'],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },
                {
                    'name': 'highmem',
                    'descr': 'Setonix highmem queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=highmem'],
                    'max_jobs': 2,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ]
                },
                {
                    'name': 'gpu',
                    'descr': 'Setonix GPU queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [], # Might need to add add rocm
                    'access': ['--partition=gpu'],
                    'max_jobs': 8,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc'
                    ],
                    'resources': [
                        {
                            'name': 'gpu',
                            'options': ['--gpus-per-node={num_gpus_per_node}']
                        }
                    ],
                },
                {
                    'name': 'gpu-dev',
                    'descr': 'Setonix GPU development queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=gpu-dev'],
                    'max_jobs': 1,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                    'resources': [
                        {
                            'name': 'gpu',
                            'options': ['--gpus-per-node={num_gpus_per_node}']
                        }
                    ],
                },
                {
                    'name': 'gpu-highmem',
                    'descr': 'Setonix GPU high memory queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=gpu-highmem'],
                    'max_jobs': 2,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                    'resources': [
                        {
                            'name': 'gpu',
                            'options': ['--gpus-per-node={num_gpus_per_node}']
                        }
                    ],
                },
            ]
        },
        {
            'name': 'joey',
            'descr': 'Joey test system',
            'hostnames': ['joey-01', 'joey-02'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'login',
                    'descr': 'Joey login node',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'modules': [],
                    'access': [],
                    'max_jobs': 1,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },
                {
                    'name': 'work',
                    'descr': 'Joey work queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=work'],
                    'max_jobs': 32,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },
                {
                    'name': 'debug',
                    'descr': 'Joey debug queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=debug'],
                    'max_jobs': 1,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ],
                },
                {
                    'name': 'highmem',
                    'descr': 'Joey highmem queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=highmem'],
                    'max_jobs': 1,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc',
                    ]
                },
                {
                    'name': 'gpu',
                    'descr': 'Joey GPU queue',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [], # Might need to add add rocm
                    'access': ['--partition=gpu'],
                    'max_jobs': 8,
                    'environs': [
                        'PrgEnv-gnu',
                        'PrgEnv-cray',
                        'PrgEnv-aocc'
                    ],
                    'resources': [
                        {
                            'name': 'gpu',
                            'options': ['--gpus-per-node={num_gpus_per_node}']
                        }
                    ]
                },
            ]
        },
        {
            'name': 'lumi',
            'descr': 'LUMI',
            'hostnames': ['ln01-nmn', 'ln02-nmn', 'ln03-nmn', 'ln04-nmn'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'login',
                    'descr': 'LUMI login node',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'modules': [],
                    'access': [],
                    'max_jobs': 1,
                    'environs': ['PrgEnv-aocc', 'PrgEnv-cray', 'PrgEnv-gnu'],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    }
                },
                {
                    'name': 'standard',
                    'descr': 'lumi work (compute nodes) partition', # Maybe add architecture
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=standard --account=project_462000053'],
                    'max_jobs': 32,
                    'environs': ['PrgEnv-aocc', 'PrgEnv-cray', 'PrgEnv-gnu'],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },
                {
                    'name': 'debug',
                    'descr': 'LUMI debug partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=debug  --account=project_462000053'],
                    'max_jobs': 1,
                    'environs': ['PrgEnv-aocc', 'PrgEnv-cray', 'PrgEnv-gnu'],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                },
                {
                    'name': 'small',
                    'descr': 'LUMI small partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'modules': [],
                    'access': ['--partition=small  --account=project_462000053'],
                    'max_jobs': 1,
                    'environs': ['PrgEnv-aocc', 'PrgEnv-cray', 'PrgEnv-gnu'],
                    'processor': {
                        'num_cpus': 256,
                        'num_cpus_per_core': 2,
                        'num_cpus_per_socket': 128,
                        'num_sockets': 2
                    },
                }
            ]
        },
        {
            'name': 'mwa',
            'descr': 'garrawarla',
            'hostnames': [
                'garrawarla'
            ],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'login',
                    'scheduler': 'local',
                    'modules': [
                        'cascadelake'
                    ],
                    'access': [],
                    'environs': [
                        'gnu'
                    ],
                    'descr': 'Garrawarla login node',
                    'max_jobs': 1,
                    'launcher': 'local'
                },
                {
                    'name': 'copyq',
                    'scheduler': 'slurm',
                    'modules': [
                        'broadwell'
                    ],
                    'access': [
                    #    '--constraint=epyc'
                    ],
                    'environs': [
                        'gnu',
                    ],
                    'descr': 'copyq partition of Garrawarla',
                    'max_jobs': 2,
                    'launcher': 'srun'
                },
                {
                    'name': 'gpuq',
                    'scheduler': 'slurm',
                    'modules': [
                        'cascadelake'
                    ],
                    'access': [
                        '--partition=gpuq',
                        '--constraint=v100'
                    ],
                    'environs': [
                        'gnu',
                        'gnu_cuda',
                        'intel',
                        'pgi'
                    ],
                    'descr': 'GPU nodes with Intel Cascadelake host',
                    'max_jobs': 4,
                    'resources': [
                        {
                            'name': '_rfm_gpu',
                            'options': [
                                '--gres=gpu:{num_gpus_per_node}'
                            ]
                        }
                    ],
                    'launcher': 'srun'
                },
                {
                    'name': 'workq',
                    'scheduler': 'slurm',
                    'modules': [
                        'cascadelake'
                    ],
                    'access': [
                        '--partition=workq'
                    ],
                    'environs': [
                        'gnu',
                        'intel'
                    ],
                    'descr': 'CPU partition with Intel Cascadelake host',
                    'max_jobs': 1,
                    'launcher': 'srun'
                }
            ]
        },
        {
            'name': 'topaz',
            'descr': 'topaz',
            'hostnames': [
                'topaz'
            ],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'login',
                    'scheduler': 'local',
                    'modules': [
                        'cascadelake'
                    ],
                    'access': [],
                    'environs': [
                        'gnu'
                    ],
                    'descr': 'Topaz login node',
                    'max_jobs': 1,
                    'launcher': 'local'
                },
                {
                    'name': 'gpuq',
                    'scheduler': 'slurm',
                    'modules': [
                        'cascadelake'
                    ],
                    'access': [
                        '--constraint=v100'
                    ],
                    'environs': [
                        'gnu',
                        'gnu_cuda',
                        'intel',
                        'pgi'
                    ],
                    'descr': 'Hybrid GPU nodes with Intel Cascadelake host',
                    'max_jobs': 4,
                    'resources': [
                        {
                            'name': '_rfm_gpu',
                            'options': [
                                '--gres=gpu:{num_gpus_per_node}'
                            ]
                        }
                    ],
                    'launcher': 'srun'
                },
                {
                    'name': 'lustreq',
                    'scheduler': 'slurm',
                    'modules': [
                        'cascadelake'
                    ],
                    'environs': [
                        'gnu',
                    ],
                    'descr': 'Hybrid GPU nodes with Intel Cascadelake host',
                    'max_jobs': 4,
                    'launcher': 'srun'
                },
                {
                    'name': 'gpuq-dev',
                    'scheduler': 'slurm',
                    'modules': [
                        'cascadelake'
                    ],
                    'access': [
                        '--partition=gpuq-dev',
                        '--constraint=v100'
                    ],
                    'environs': [
                        'gnu',
                        'gnu_cuda',
                        'intel',
                        'pgi'
                    ],
                    'descr': 'Hybrid GPU Devel nodes with Intel Cascadelake host',  # noqa: E501
                    'max_jobs': 1,
                    'resources': [
                        {
                            'name': '_rfm_gpu',
                            'options': [
                                '--gres=gpu:{num_gpus_per_node}'
                            ]
                        }
                    ],
                    'launcher': 'srun'
                },
                {
                    'name': 'nvlinkq',
                    'scheduler': 'slurm',
                    'modules': [
                        'broadwell'
                    ],
                    'access': [
                        '--constraint=p100'
                    ],
                    'environs': [
                        'gnu',
                        'gnu_cuda',
                        'intel',
                        'pgi'
                    ],
                    'descr': 'Pascal GPU nodes with Intel Broadwell host',
                    'max_jobs': 4,
                    'resources': [
                        {
                            'name': '_rfm_gpu',
                            'options': [
                                '--gres=gpu:{num_gpus_per_node}'
                            ]
                        }
                    ],
                    'launcher': 'srun'
                },
                {
                    'name': 'nvlinkq-dev',
                    'scheduler': 'slurm',
                    'modules': [
                        'broadwell'
                    ],
                    'access': [
                        '--partition=nvlinkq-dev',
                        '--constraint=p100'
                    ],
                    'environs': [
                        'gnu',
                        'gnu_cuda',
                        'intel',
                        'pgi'
                    ],
                    'descr': 'Pascal GPU Devel nodes with Intel Broadwell host',  # noqa: E501
                    'max_jobs': 1,
                    'resources': [
                        {
                            'name': '_rfm_gpu',
                            'options': [
                                '--gres=gpu:{num_gpus_per_node}'
                            ]
                        }
                    ],
                    'launcher': 'srun'
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'PrgEnv-cray',
            'target_systems': ['setonix', 'joey'],
            'modules': [
                'PrgEnv-cray',
                'cray-mpich/8.1.30',
            ]
        },
        {
            'name': 'PrgEnv-gnu',
            'target_systems': ['setonix', 'joey'],
            'modules': [
                'PrgEnv-gnu',
                'cray-mpich/8.1.30',
            ]
        },
        {
            'name': 'PrgEnv-aocc',
            'target_systems': ['setonix', 'joey'],
            'modules': [
                'PrgEnv-aocc',
                'cray-mpich/8.1.30',
            ]
        },
        {
            'name': 'gnu11.1',
            'target_systems': ['mulan'],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'gnu12.0',
            'target_systems': ['mulan'],
            'cc': 'gcc -I/pawsey/mulan/raw-builds/GCC/11.1.0/include -pthread -Wl,-rpath ' +
                  '-Wl,/pawsey/mulan/raw-builds/GCC/11.1.0/lib -Wl,--enable-new-dtags ' +
                  '-L/pawsey/mulan/raw-builds/GCC/11.1.0/lib -lmpi ' +
                  '-I/pawsey/mulan/raw-builds/GCC/12.0.0/include -L/pawsey/mulan/raw-builds/GCC/12.0.0/lib',
            'cxx': 'g++ -I/pawsey/mulan/raw-builds/GCC/11.1.0/include -pthread -Wl,-rpath ' +
                   '-Wl,/pawsey/mulan/raw-builds/GCC/11.1.0/lib -Wl,--enable-new-dtags ' +
                   '-L/pawsey/mulan/raw-builds/GCC/11.1.0/lib -lmpi_cxx -lmpi ' +
                   '-I/pawsey/mulan/raw-builds/GCC/12.0.0/include -L/pawsey/mulan/raw-builds/GCC/12.0.0/lib',
            'ftn': 'gfortran -I/pawsey/mulan/raw-builds/GCC/11.1.0/include -pthread -Wl-rpath ' +
                   '-Wl,/pawsey/mulan/raw-builds/GCC/11.1.0/lib -Wl,--enable-new-dtags ' +
                   '-I/pawsey/mulan/raw-builds/GCC/11.1.0/lib -L/pawsey/mulan/raw-builds/GCC/11.1.0/lib ' +
                   '-lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi ' +
                   '-I/pawsey/mulan/raw-builds/GCC/12.0.0/include -L/pawsey/mulan/raw-builds/GCC/12.0.0/lib ' +
                   '-I/pawsey/mulan/raw-builds/GCC/12.0.0/lib'
        },
        {
            'name': 'clang13.0',
            'target_systems': ['mulan'],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': ''
        },
        {
            'name': 'clang14.0',
            'target_systems': ['mulan'],
            'cc': 'clang -I/pawsey/mulan/raw-builds/CLANG/13.0.0/include -pthread -Wl,-rpath ' +
                  '-Wl,/pawsey/mulan/raw-builds/CLANG/13.0.0/lib -Wl,--enable-new-dtags ' +
                  '-L/pawsey/mulan/raw-builds/CLANG/13.0.0/lib -lmpi ' +
                  '-I/pawsey/mulan/raw-builds/CLANG/14.0.0/include -L/pawsey/mulan/raw-builds/CLANG/14.0.0/lib',
            'cxx': 'clang++ -I/pawsey/mulan/raw-builds/CLANG/13.0.0/include -pthread -Wl,-rpath ' +
                   '-Wl,/pawsey/mulan/raw-builds/CLANG/13.0.0/lib -Wl,--enable-new-dtags ' +
                   '-L/pawsey/mulan/raw-builds/CLANG/13.0.0/lib -lmpi_cxx -lmpi ' +
                   '-I/pawsey/mulan/raw-builds/CLANG/14.0.0/include -L/pawsey/mulan/raw-builds/CLANG/14.0.0/lib',
            'ftn': ''
        },
        {
            'name': 'aocc3.0',
            'target_systems': ['mulan'],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': ''
        },
        {
            'name': 'aocc3.2',
            'target_systems': ['mulan'],
            'cc': 'clang -I/pawsey/mulan/raw-builds/CLANG/AOCC-3.0/include -pthread -Wl,-rpath ' +
                  '-Wl,/pawsey/mulan/raw-builds/CLANG/AOCC-3.0/lib -Wl,--enable-new-dtags ' + 
                  '-L/pawsey/mulan/raw-builds/CLANG/AOCC-3.0/lib -lmpi ' +
                  '-I/pawsey/mulan/raw-builds/CLANG/AOCC-3.2/include -L/pawsey/mulan/raw-builds/CLANG/AOCC-3.2/lib',
            'cxx': 'clang++ -I/pawsey/mulan/raw-builds/CLANG/AOCC-3.0/include -pthread -Wl,-rpath ' +
                   '-Wl,/pawsey/mulan/raw-builds/CLANG/AOCC-3.0/lib -Wl,--enable-new-dtags ' +
                   '-L/pawsey/mulan/raw-builds/CLANG/AOCC-3.0/lib -lmpi_cxx -lmpi ' +
                   '-I/pawsey/mulan/raw-builds/CLANG/AOCC-3.2/include -L/pawsey/mulan/raw-builds/CLANG/AOCC-3.2/lib',
            'ftn': ''
        },
        {
            'name': 'gnu',
            'target_systems': [
                'mwa'
            ],
            'modules': [
                'gcc/8.3.0'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'gnu_cuda',
            'target_systems': [
                'mwa'
            ],
            'modules': [
                'gcc/8.3.0',
                'cuda/10.2',
                'openmpi-ucx/4.0.3'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'intel',
            'target_systems': [
                'mwa'
            ],
            'modules': [
                'intel',
                'openmpi-ucx/4.0.3'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'pgi',
            'target_systems': [
                'mwa'
            ],
            'modules': [
                'pgi'
            ],
            'cc': 'pgcc',
            'cxx': 'pgc++',
            'ftn': 'pgf90'
        },
        {
            'name': 'gnu',
            'target_systems': [
                'topaz','fuggles-topaz'
            ],
            'modules': [
                'gcc/8.3.0',
                'openmpi-ucx-gpu/4.0.2'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'gnu_cuda',
            'target_systems': [
                'topaz','fuggles-topaz'
            ],
            'modules': [
                'gcc/8.3.0',
                'openmpi-ucx-gpu/4.0.2',
                'cuda/10.1'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'intel',
            'target_systems': [
                'topaz', 'fuggles-topaz'
            ],
            'modules': [
                'intel',
                'openmpi-ucx-gpu/4.0.2'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'pgi',
            'target_systems': [
                'topaz','fuggles-topaz'
            ],
            'modules': [
                'pgi'
            ],
            'cc': 'pgcc',
            'cxx': 'pgc++',
            'ftn': 'pgf90'
        },
        {
            'name': 'gnu',
            'target_systems': [
                'zeus','fuggles-zeus'
            ],
            'modules': [
                'gcc/8.3.0',
                'openmpi/2.1.2'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'intel',
            'target_systems': [
                'zeus','fuggles-zeus'
            ],
            'modules': [
                'intel',
                'openmpi/2.1.2'
            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },

        {
            'name': 'PrgEnv-cray',
            'target_systems': ['lumi'],
            'modules': [
                'PrgEnv-cray',
                'cray-mpich'
            ],
        },
        {
            'name': 'PrgEnv-gnu',
            'target_systems': ['lumi'],
            'modules': [
                'PrgEnv-gnu',
                'cray-mpich'
            ],
        },
        {
            'name': 'PrgEnv-aocc',
            'target_systems': ['lumi'],
            'modules': [
                'PrgEnv-aocc',
                'cray-mpich'
            ],
        },

        {
            'name': 'PrgEnv-cray',
            'modules': [
                'PrgEnv-cray',
                'cray-mpich/7.7.0'
            ],
            'variables': [
                [
                    'CRAYPE_LINK_TYPE',
                    'dynamic'
                ]
            ]
        },
        {
            'name': 'PrgEnv-gnu',
            'modules': [
                'PrgEnv-gnu',
                'cray-mpich/7.7.0'
            ],
            'variables': [
                [
                    'CRAYPE_LINK_TYPE',
                    'dynamic'
                ]
            ]
        },
        {
            'name': 'PrgEnv-intel',
            'modules': [
                'PrgEnv-intel',
                'cray-mpich/7.7.0'
            ],
            'variables': [
                [
                    'CRAYPE_LINK_TYPE',
                    'dynamic'
                ]
            ]
        },
        {
            'name': 'PrgEnv-pgi',
            'modules': [
                'PrgEnv-pgi',
                'cray-mpich/7.7.0'
            ],
            'variables': [
                [
                    'CRAYPE_LINK_TYPE',
                    'dynamic'
                ]
            ]
        },
        {
            'name': 'builtin',
            'cc': 'cc',
            'cxx': '',
            'ftn': ''
        },
        {
            'name': 'builtin-gcc',
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        }
    ],
    'logging': [
        {
            'level': 'debug',
            'handlers': [
                {
                    'type': 'file',
                    'name': 'reframe.log',
                    'level': 'debug',
                    'format': '[%(asctime)s] %(levelname)s: %(check_name)s: %(message)s',  # noqa: E501
                    'append': False
                },
                {
                    'type': 'stream',
                    'name': 'stdout',
                    'level': 'info',
                    'format': '%(message)s'
                },
                {
                    'type': 'file',
                    'name': 'reframe.out',
                    'level': 'info',
                    'format': '%(message)s',
                    'append': False
                }
            ],
            'handlers_perflog': [
                {
                    'type': 'filelog',
                    'prefix': '%(check_system)s/%(check_partition)s',
                    'level': 'info',
                    'format': '%(asctime)s|reframe %(version)s|%(check_info)s|jobid=%(check_jobid)s|%(check_perf_var)s=%(check_perf_value)s|ref=%(check_perf_ref)s (l=%(check_perf_lower_thres)s, u=%(check_perf_upper_thres)s)',  # noqa: E501
                    'append': True
                }
            ]
        }
    ],
    'modes': [
        {
            'name': 'maintenance',
            'options': [
                '--exec-policy=async',
                '--reservation=maintenance',
                '--save-log-files',
                '--tag=acceptance',
                '--timestamp=%F_%H-%M-%S'
            ]
        },
        {
            'name': 'production',
            'options': [
                '--exec-policy=async',
                '--strict',
                '--output=$APPS/UES/$USER/regression/production',
                '--logdir=$APPS/UES/$USER/regression/production/logs',
                '--stage=$SCRATCH/regression/production/stage',
                '--save-log-files',
                '--tag=production',
                '--timestamp=%F_%H-%M-%S'
            ]
        }
    ],
    'general': [
        {
            'check_search_path': [
                'checks/'
            ],
            'check_search_recursive': True
        }
    ]
}
