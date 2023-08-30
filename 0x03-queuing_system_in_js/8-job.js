const createPushNotificationsJobs = (jobs, queue) => {
  if (jobs.constructor !== Array) throw Error("Jobs is not an array");
  jobs.forEach((job) => {
    let jobCreated = queue
      .create("push_notification_code_2", job)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${jobCreated.id}`);
      })
      .on("complete", () => {
        console.log(`Notification job ${jobCreated.id} completed`);
      })
      .on("progress", (progress, _data) => {
        console.log(`Notification job ${jobCreated.id} ${progress}% complete`);
      })
      .on("failure", (err) => {
        console.log(`Notification job ${jobCreated.id} failed: ${err}`);
      });
  });
};

module.exports = createPushNotificationsJobs;
