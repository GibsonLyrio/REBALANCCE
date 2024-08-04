import Router from "express"
import eventsRouter from "./events.mjs"
import helloRouter from "./hello.mjs"
import loginRouter from "./login.mjs"

const routes = Router()

routes.use('/events', eventsRouter)
routes.use('/hello', helloRouter)
routes.use('/login', loginRouter)

export default routes
