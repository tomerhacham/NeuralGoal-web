ECHO "Compailing"
python -m grpc_tools.protoc -I="C:\Project\NeuralGoal-web\Server\protocs" --python_out=. --grpc_python_out=. "C:\Project\NeuralGoal-web\Server\protocs\match.proto"
PAUSE
