import pg from 'pg'
import 'dotenv/config'

const { Pool } = pg

const dbConnectionUrl = process.env.connectionString;

export const db = new Pool({
  connectionString: dbConnectionUrl
})
