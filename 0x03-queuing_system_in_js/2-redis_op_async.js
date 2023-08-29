import { createClient, print } from "redis";
import { promisify } from "util";
const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const asyncGet = promisify(client.get).bind(client)(schoolName);
  console.log(await asyncGet);
}

async function main() {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  displaySchoolValue("HolbertonSanFrancisco");
}

main();
