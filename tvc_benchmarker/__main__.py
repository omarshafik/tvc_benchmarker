import tvc_benchmarker
import matplotlib as mpl 
mpl.use('agg')
import sys
sys.path.append("D:\\NeuroscienceLocal\\fs\\functional-similarity\\src")
import funcsimilarity as fs

params = {
    '0': {   
        'name': 'FS-1',
        'method': 'fs.estimate_connectivity_in_parallel',
        'params': { 
            'window_size': 1
        }
    },
    '1': {   
        'name': 'FS-5',
        'method': 'fs.estimate_connectivity_in_parallel',
        'params': { 
            'window_size': 5
        }
    },
    '2': {   
        'name': 'FS-15',
        'method': 'fs.estimate_connectivity_in_parallel',
        'params': { 
            'window_size': 15
        }
    },
    '3': {   
        'name': 'FS-29',
        'method': 'fs.estimate_connectivity_in_parallel',
        'params': { 
            'window_size': 29
        }
    }
}
tvc_benchmarker.run_simulations('2.0',
    output_dir="./results/2.0",
    usesaved='no',
    new_method=[fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel], 
    params_new_method=params)

tvc_benchmarker.run_simulations('2.1',
    output_dir="./results/2.1",
    usesaved='no',
    new_method=[fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel], 
    params_new_method=params)

tvc_benchmarker.run_simulations('2.2',
    output_dir="./results/2.2",
    usesaved='no',
    new_method=[fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel], 
    params_new_method=params)

tvc_benchmarker.run_simulations('2.3',
    output_dir="./results/2.3",
    usesaved='no',
    new_method=[fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel, fs.estimate_connectivity_in_parallel], 
    params_new_method=params)
