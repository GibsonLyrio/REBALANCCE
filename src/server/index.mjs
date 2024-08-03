import express from 'express'
import routes from './routes/index.mjs'
import 'dotenv/config'

const app = express();
const PORT = process.env.PORT || 3000

app.use(routes)


app.listen(PORT, { host: '0.0.0.0' }, () => {
  console.log(`Running on port ${PORT}`)
})
