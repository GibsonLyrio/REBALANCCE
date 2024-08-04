import Router from 'express'
import cookieParser from 'cookie-parser'
import session from 'express-session'
import passport from 'passport'
import '../strategies/local_strategy.mjs'

const loginRouter = Router()

loginRouter.use(cookieParser())
loginRouter.use(
  session({
    secret: 'a',
    saveUninitialized: false,
    resave: false,
    cookie: {
      maxAge: (60000 * 60),
    }
  })
)
loginRouter.use(passport.initialize())
loginRouter.use(passport.session())

loginRouter.post(
  '/',
  passport.authenticate('local'),
  (req, res) => {
    return res.sendStatus(200)
  }
)

loginRouter.get('/status', (req, res) => {
  console.log(`Inside /auth/status/ endpoint with user ${req.user}`)
  if (req.user) {
    console.log(req.user);
    return res.send(req.user)
  }
  return res.sendStatus(401)
})

loginRouter.post('/logout', (req, res) => {
  if(!req.user) return res.sendStatus(401)
  req.logout((err) => {
    if (err) return res.sendStatus(400)
    res.sendStatus(200)
  })
})

export default loginRouter
