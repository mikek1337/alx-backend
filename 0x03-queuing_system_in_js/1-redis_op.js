import { createClient } from 'redis';

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
}).on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
})


async function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        console.log(`Reply: ${reply}`);
    })

}

async function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        console.log(reply)
    })
}

