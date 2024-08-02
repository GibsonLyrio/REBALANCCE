// importing Unique Universal ID
import { randomUUID } from "node:crypto"

export class DataBase {
  #events = new Map()

  add_new_event(event_info){
    const event_id = randomUUID()
    this.#events.set(event_id, event_info)
  }

  list_events(filter = false){
    if(!filter){
      return Array.from(this.#events.entries()).map((event_array) => {
        const event_id = event_array[0]
        const event_info = event_array[1]

        return {
          event_id,
          ...event_info
        }
      })
    }
  }

}
