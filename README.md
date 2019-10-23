# MERL: Multi-Head Reinforcement Learning

This repository has been forked from [OpenAI baselines](https://github.com/openai/baselines).
## Prerequisites 
MERL requires python3 (>=3.5) with the development headers. You'll also need system packages CMake, OpenMPI and zlib. Those can be installed as follows
### Ubuntu 
    
```bash
sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev
```
    
### Mac OS X
Installation of system packages on Mac requires [Homebrew](https://brew.sh). With Homebrew installed, run the following:
```bash
brew install cmake openmpi
```
    
## Virtual environment
From the general python package sanity perspective, it is a good idea to use virtual environments (virtualenvs) to make sure packages from different projects do not interfere with each other. You can install virtualenv (which is itself a pip package) via
```bash
pip install virtualenv
```
Virtualenvs are essentially folders that have copies of python executable and all python packages.
To create a virtualenv called venv with python3, one runs 
```bash
virtualenv /path/to/venv --python=python3
```
To activate a virtualenv: 
```
. /path/to/venv/bin/activate
```
More thorough tutorial on virtualenvs and options can be found [here](https://virtualenv.pypa.io/en/stable/) 


## Installation
- Clone the repo and cd into it:
    ```bash
    git clone https://github.com/neurips-2019-id-4790/MERL.git
    cd MERL
    ```
- If you don't have TensorFlow installed already, install your favourite flavor of TensorFlow. In most cases, 
    ```bash 
    pip install tensorflow-gpu # if you have a CUDA-compatible gpu and proper drivers
    ```
    or 
    ```bash
    pip install tensorflow
    ```
- Install MERL package
    ```bash
    pip install -e .
    ```
    
### MuJoCo
[MuJoCo](http://www.mujoco.org) (multi-joint dynamics in contact) physics simulator is proprietary and requires binaries and a license (temporary 30-day license can be obtained from [www.mujoco.org](http://www.mujoco.org)). Instructions on setting up MuJoCo can be found [here](https://github.com/openai/mujoco-py)

## Training models
You can start a simulation on the environment of your choice (eg. HalfCheetah-v2, ) like so:
```bash
python -m baselines_merl.run --alg=<name of the algorithm> --env=<environment_id> [additional arguments]
```
### Example 1. PPO with MuJoCo HalfCheetah
For instance, to train a fully-connected network controlling MuJoCo HalfCheetah using PPO for 1M timesteps
```bash
python -m baselines_merl.run --alg=ppo2 --env=HalfCheetah-v2 --network=mlp --num_timesteps=1e6
```
Note that for mujoco environments fully-connected network is default, so we can omit `--network=mlp`
The hyperparameters for both network and the learning algorithm can be controlled via the command line, for instance:
```bash
python -m baselines_merl.run --alg=ppo2 --env=HalfCheetah-v2 --network=mlp --num_timesteps=2e7 --ent_coef=0.1 --num_hidden=32 --num_layers=3 --value_network=copy
```
will set entropy coefficient to 0.1, and construct fully connected network with 3 layers with 32 hidden units in each, and create a separate network for value function estimation (so that its parameters are not shared with the policy network, but the structure is the same)

See docstrings in [common/models.py](baselines_merl/common/models.py) for description of network parameters for each type of model, and 
docstring for [baselines_merl/ppo2/ppo2.py/learn()](baselines_merl/ppo2/ppo2.py#L152) for the description of the ppo2 hyperparameters. 

### Example 2. PPO+MERL with MuJoCo HalfCheetah
To run our PPO+MERL implementation on HalfCheetah:
```
python -m baselines_merl.run --alg=ppo2_merl --env=HalfCheetah-v2 --num_timesteps=1e6
```

### Run sets of experiments
To run sets of experiments (different envs & different seeds):
```
bash run.sh
```

## Saving, loading and visualizing models
To save:
```bash
python -m baselines_merl.run --alg=ppo2_merl --env=HalfCheetah-v2 --num_timesteps=1e6 --save_path=~/models/halfcheetah_1M_ppomerl
```
To visualize:
```bash
python -m baselines_merl.run --alg=ppo2_merl --env=HalfCheetah-v2 --num_timesteps=0 --load_path=~/models/halfcheetah_1M_ppomerl --play
```
To load:
```bash
python -m baselines_merl.run --alg=ppo2_merl --env=HalfCheetah-v2 --num_timesteps=1e6 --load_path=~/models/halfcheetah_1M_ppomerl
```

*NOTE:* Mujoco environments require normalization to work properly, so we wrap them with VecNormalize wrapper. Currently, to ensure the models are saved with normalization (so that trained models can be restored and run without further training) the normalization coefficients are saved as tensorflow variables. This can decrease the performance somewhat, so if you require high-throughput steps with Mujoco and do not need saving/restoring the models, it may make sense to use numpy normalization instead. To do that, set `use_tf=False` in [baselines_merl/run.py](baselines_merl/run.py#L116).


## Paper
For a detailed description of the architecture please read [our paper](https://hal.inria.fr/hal-02305105/document).

```
@inproceedings{fletberliac2019merl,
  title={MERL: Multi-Head Reinforcement Learning},
  author={Flet-Berliac, Yannis and Preux, Philippe},
  booktitle={Deep Reinforcement Learning Workshop (NeurIPS 2019)},
  year={2019}
}
```
