import { DataBase } from "./database_memory.js"
const database = new DataBase

// creating manually a event:
database.add_new_event({
  type: 'revenue',
  value: 320,
  data: '10/08/2024'
})
// ----

// define de JSON schemas:
const response_schema = {
  response: {
    200: {
      properties: {
        message: { type: 'string' }
      },
      required: [ 'message' ]
    }
  }
}

// config de events controller router:
export const events_controller = (server, options, done) => {
  server.get('/', (req, reply) => {

    return {
      transacoes: database.list_events()
    }
  })

  server.get('/hello/:name', (req, reply) => {
    return {
      message: `Hello ${req.params.name}`
    }
  })

  done()
}
// ----
