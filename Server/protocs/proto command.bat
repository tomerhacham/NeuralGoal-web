ECHO "Compailing"
python -m grpc_tools.protoc -I="C:\Users\Tomer Hacham\Desktop\gRPC\protocs" --python_out=. --grpc_python_out=. "C:\Users\Tomer Hacham\Desktop\gRPC\protocs\match.proto"
PAUSE
