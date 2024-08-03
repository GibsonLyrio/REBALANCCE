import Router from 'express'

const eventsRouter = Router()

// some middleware specific for this eventsRouter
eventsRouter.use((req, res, next) => {
  console.log('Now time: ', Date.now())
  next()
})

// define homepage route
eventsRouter.get('/', (req, res) => {
  return res.status(200).send({ message: 'This is home page of events' })
})

// define help route
eventsRouter.get('/help/', (req, res) => {
  return res.status(200).send({ message: 'This is help page of events' })
})

export default eventsRouter
