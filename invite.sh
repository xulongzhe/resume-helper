DIR=$(cd "$(dirname "$0")";pwd)
cd ${DIR}/src
python3 invite.py $@
