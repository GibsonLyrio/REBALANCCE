import { fastify } from "fastify"
import { events_controller } from "./events_controller.js"


// creating server and database instances:
const server = fastify()

// define the controllers pluggins:
server.register(events_controller, { prefix: '/events' })

// try execute de server in home network:
try {
  server.listen({ port: 3000, host: '0.0.0.0' })  // server ON;
} catch (error) {
  server.log.error(error)
  process.exit(1)   // if has some thing wrong, kill server; 
}
// ----