import Router from "express"
import eventsRouter from "./events.mjs"
import helloRouter from "./hello.mjs"

const routes = Router()

routes.use('/events', eventsRouter)
routes.use('/hello', helloRouter)

export default routes
