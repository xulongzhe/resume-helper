DIR=$(cd "$(dirname "$0")";pwd)
cd ${DIR}
python3 forward.py $@
