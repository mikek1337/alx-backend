import createPushNotificationsJobs from "./8-job";
import { createQueue } from "kue";
import { expect } from "chai";
import sinon from "sinon";

const queue = createQueue();

describe("createPushNotificationsJobs", () => {
  // using queue.test mode
  beforeEach(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.exit();
  });
  it("display a error message if jobs is not an array", () => {
    const spy = sinon.spy(console, "log");
    createPushNotificationsJobs("jobs", queue);
    expect(spy.calledWith("Jobs is not an array")).to.throws(Error("Jobs is not an array"))
    spy.restore();
  });
  it("create two new jobs to the queue", () => {
    createPushNotificationsJobs(
      [
        {
          phoneNumber: "4153518780",
          message: "This is the code 1234 to verify your account",
        },
        {
          phoneNumber: "4153518781",
          message: "This is the code 4562 to verify your account",
        },
      ],
      queue
    );
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_2");
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: "4153518780",
      message: "This is the code 1234 to verify your account",
    });
    expect(queue.testMode.jobs[1].type).to.equal("push_notification_code_2");
    expect(queue.testMode.jobs[1].data).to.eql({
      phoneNumber: "4153518781",
      message: "This is the code 4562 to verify your account",
    });
  });
});
