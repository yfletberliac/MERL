#!/bin/bash


declare -a envs=("HalfCheetah-v2") # Choose a list of envs
declare -a seeds=("0" "1" "10" "11" "100" "101" "110" "111") # Choose a list of different seeds

for env in "${envs[@]}"
do
for seed in "${seeds[@]}"
do

    OPENAI_LOGDIR=logs/experiment01/$env-PPO-$seed OPENAI_LOG_FORMAT=csv,tensorboard,stdout python -m baselines_merl.run --alg=ppo2 --network='mlp' --env=$env --num_timesteps=1e6 --seed $seed --num_env 1 --ent_coef=0.0 --nsteps=2048 --nminibatches=32 --noptepochs=15 --log_interval=1 --cliprange=0.2 --value_network='copy' --lr=3e-4 --nfs=1 --fs_coef=0.01 --ve_coef 0.5 &
    OPENAI_LOGDIR=logs/experiment01/$env-PPOMERL-$seed OPENAI_LOG_FORMAT=csv,tensorboard,stdout python -m baselines_merl.run --alg=ppo2_merl --network='mlp' --env=$env --num_timesteps=1e6 --seed $seed --num_env 1 --ent_coef=0.0 --nsteps=2048 --nminibatches=32 --noptepochs=15 --log_interval=1 --cliprange=0.2 --value_network='copy' --lr=3e-4 --nfs=1 --fs_coef=0.01 --ve_coef 0.5

done
sleep 10
done
