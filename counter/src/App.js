import React from 'react'
import { Route } from "react-router-dom" 
import { Counter, Todo } from 'components/index'

const App = () => {
  return (<div>
    <Route exact path='/' component={Counter}/>
    <Route exact path='/todo' component={Todo}/>
    </div>)
}

export default App;
