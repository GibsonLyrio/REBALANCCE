import helloValidationSchema from '../utils/validation_schemas.mjs'
import { validationResult, checkSchema } from 'express-validator'
import Router from "express"


const helloRouter = Router()

helloRouter.get('/', checkSchema(helloValidationSchema), (req, res) => {
  const result = validationResult(req)
  if (!result.isEmpty()) {
    return res.status(400).send({ badRequest: result })
  }
  return res.status(200).send(`Hello ${req.query.name}`)
})

export default helloRouter
