import asyncio
import json
import websockets

SEQUENCER_URI = "wss://arb1.arbitrum.io/feed"

async def watch_sequencer_feed():
    print("Starting sequencer feed watcher")

    async with websockets.connect(uri=SEQUENCER_URI, ping_timeout=None) as websocket:
        while True:
            try:
                sequencer_payload = json.loads(await websocket.recv())
            except Exception as e:
                print(f"(watch_new_blocks) websocket.recv(): {e}")
                print(sequencer_payload)
                break
            else:
                try:
                    messages = sequencer_payload["messages"]
                except KeyError as e:
                    continue
                else:
                    for message in messages:
                        print(message)

if __name__ == "__main__":
    asyncio.run(watch_sequencer_feed())
    print("Complete")
