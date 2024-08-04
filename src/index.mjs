import Express from 'express'
import routes from './routes/index.mjs'
import 'dotenv/config'

const express = Express();
const PORT = process.env.PORT || 3000

express.use(Express.json())
express.use(routes)

express.listen(PORT, { host: '0.0.0.0' }, () => {
  console.log(`Running on port ${PORT}`)
})
