import passport from "passport"
import { Strategy } from "passport-local"
import { mockUsers } from "../utils/constants.mjs"

passport.serializeUser((user, done) => {
  console.log(`Inside serialize user with ID: ${user.id}`)
  done(null, user.id)
})

passport.deserializeUser((id, done) => {
  console.log(`Inside deserialize user with ID:${id}`)
  try {
    const findUser = mockUsers.find((user) => user.id === id)
    if (!findUser) throw new Error('User not found')
    done(null, findUser)
  } catch (err) {
    done(err, null)
  }
})

export default passport.use(
  new Strategy((username, password, done) => {
    console.log({ username: username, password: password })
    try {
      const findUser = mockUsers.find(
        (user) => user.username === username
      )
      if (!findUser) throw new Error('User not found')
      if (findUser.password !== password) throw new Error('Bad credentials')
      console.log(findUser)
      done(null, findUser)
    } catch (err) {
      done(err, null)
    }
  })
)
