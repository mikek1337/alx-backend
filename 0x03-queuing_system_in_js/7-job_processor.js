import { createQueue } from "kue";

const queue = createQueue();

const blackListed = ["4153518780", "4153518781"];

const sendNotification = (phoneNumber, message, job, done) => {
    let total = 2, pending = 2;
    if (blackListed.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
        clearInterval(sendInterval);
        return;
    }
    let sendInterval = setInterval(() => {
        if (total - pending <= total / 2) {
            job.progress(total - pending, total);
        }


        console.log(`Sending notification to ${phoneNumber} with message ${message}`)

        --pending || done();
        pending || clearInterval(sendInterval);
    }, 100);
};

queue.process("push_notification_code_2", 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
