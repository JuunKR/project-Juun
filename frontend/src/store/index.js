import { createStore } from 'redux'
import TodoReducer from './TodoReducer'
export {default as TodoReducer} from './TodoReducer'
export const store = createStore(TodoReducer)