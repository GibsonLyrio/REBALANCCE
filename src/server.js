import { fastify } from "fastify"
import { DataBase } from "./database_memory.js"


const server = fastify()
const database = new DataBase
database.add_new_event({
  type: "revenue",
  value: 320,
  data: "10/08/2024"
})


server.get('/', (request, reply) => {
  console.log(database.list_events());

  reply.status(200).send('Home page [GET]')
})

server.put('/', (request, reply) => {
  reply.send(' Home page [PUT]')
})

try {
  server.listen({ port: 3000, host: '0.0.0.0' })
} catch (error) {
  server.log.error(error)
  process.exit(1)
}
