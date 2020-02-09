#!/usr/bin/env bash

#declare -a UNSET_ENVS=() ENVS=(
#    'BITCOINPAY_API_KEY'
#)
#
#echo "Checking that all required environment variables are set..."
#
#for env in ${ENVS[@]}; do
#    [ -z "${!env}" ] && echo "$env is unset!" && UNSET_ENVS+=("$env")
#done
#
#if [ ${#UNSET_ENVS} -ne 0 ] && [ -n "${PRODUCTION}" ]; then
#    echo "Aborting the release."
#    exit 1
#fi

#echo "Checking migrations..."
#./manage.py makemigrations --check
#exit_code=$?
#
#if [ $exit_code -ne 0 ]; then
#    echo "Models have changes that are not reflected in migrations yet."
#    echo "Aborting the release."
#    exit $exit_code
#fi

echo "Making migrations..."
./manage.py makemigrations || exit $?

echo "Running migrations..."
./manage.py migrate || exit $?

#echo "Invalidating cache..."
#./manage.py invalidate_cache || exit $?

echo "Done!"
exit 0

