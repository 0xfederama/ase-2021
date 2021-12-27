const {
  Client,
  logger,
  Variables
} = require("camunda-external-task-client-js");

// configuration for the Client:
//  - 'baseUrl': url to the Workflow Engine
//  - 'logger': utility to automatically log important events
const config = {
  baseUrl: "http://localhost:8080/engine-rest",
  use: logger
};

// create a Client instance with custom configuration
const client = new Client(config);

const handler = async({ task, taskService }) => {
  // Put your business logic here
  const variables = new Variables()

  if (Math.random() > 0.5) {
    console.log("[Germanic Tribe Fighter] Tha battle has lost!");
    variables.set("legionStatus", "defeated");
  } else {
    console.log("[Germanic Tribe Fighter] The Roman Legions has won the battle!");
    variables.set("legionStatus", "victorious");
  }

  // Complete the task
  try {
    await taskService.complete(task, variables);
    console.log("Task completed.");
  } catch(e) {
    console.error(`Failed completing task ${e}`);
  }
};

// susbscribe to the topic: "FightTribe"
client.subscribe("FightTribe", handler);
