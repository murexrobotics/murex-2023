# import controller
# import emergency
# from thrust_vectoring import maximzed_thrust_vectoring, vertical_thrust
import command
import asyncio

# emergency.register(
#     telemetry_target="bme680.temperature",
#     min=10,
#     max=20
# )

asyncio.run(command.start())





