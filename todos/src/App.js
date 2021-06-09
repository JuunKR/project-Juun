import { Route } from 'react-router-domyarn'
import { Schedule } from './containers'

const App = () =>{
  return (
    <div>
      <Route exact path ='/' component={ Schedule }/>
    </div>)
}
export default App