import Express, { response } from 'express'
import routes from './routes/index.mjs'
import 'dotenv/config'
import cookieParser from 'cookie-parser'
import session from 'express-session'
import passport from 'passport'
import './strategies/local_strategy.mjs'

const express = Express();
const PORT = process.env.PORT || 3000

express.use(Express.json())
express.use(cookieParser())
express.use(
  session({
    secret: 'a',
    saveUninitialized: false,
    resave: false,
    cookie: {
      maxAge: (60000 * 60),
    }
  })
)
express.use(passport.initialize())
express.use(passport.session())
express.use(routes)

express.post(
  '/api/auth',
  passport.authenticate('local'),
  (req, res) => {
    return res.sendStatus(200)
  }
)

express.get('/api/auth/status', (req, res) => {
  console.log(`Inside /auth/status/ endpoint with user ${req.user}`)
  if (req.user) {
    console.log(req.user);
    return res.send(req.user)
  }
  return res.sendStatus(401)
})

express.post('/api/auth/logout', (req, res) => {
  if(!req.user) return res.sendStatus(401)
  req.logout((err) => {
    if (err) return res.sendStatus(400)
    res.sendStatus(200)
  })
})

express.listen(PORT, { host: '0.0.0.0' }, () => {
  console.log(`Running on port ${PORT}`)
})
