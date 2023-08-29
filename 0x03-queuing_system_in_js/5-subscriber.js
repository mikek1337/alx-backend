import { createClient } from "redis";

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

client.subscribe("holberton school channel", (err, count) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`Subscribed to ${count} channel`);
  }
});

client.on("message", (channel, message) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    client.unsubscribe(channel);
    client.quit();
  }
});
