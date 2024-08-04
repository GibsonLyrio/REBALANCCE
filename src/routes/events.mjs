import Router, { json } from 'express'
import { db } from '../db.mjs'

const eventsRouter = Router()

eventsRouter.get('/', async (req, res) => {
  const { rows: books } = await db.query('SELECT * FROM books')
  return res.status(200).send({ books: books })
})

export default eventsRouter
