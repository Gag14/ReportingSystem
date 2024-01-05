// import { useEffect, useState } from 'react';
import './App.css';
// import  axios from "axios"
import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage"
import NoPage from './pages/NoPage';
import HomePage from './pages/HomePage/HomePage';
// const baseURL =  'https://jsonplaceholder.typicode.com/';

function App() {
  return (

    <BrowserRouter>
      <Routes>
        <Route path="/">
          <Route index element={<LoginPage />} />
          <Route path="homepage" element={<HomePage />} />
          <Route path='' />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
  // const [email,setEmail] = useState('')
  // const [password,setPassword] = useState('')
  // const [posts, setPosts] = useState(null)
  // const [loading, setLoading] = useState(false)
  // const [errorMessage, setErrorMessage] = useState(null)
  // useEffect(() => {
  //   // setLoading(true)
  //     axios.get(baseURL+ 'posts').then(({data}) => {
  //       setPosts(data)
  //       // setErrorMessage(null)
  //     }).catch(() => {
  //       // setErrorMessage("Error Message")
  //       setPosts(null)
  //    })
  //    //.finally(() => {
  //     //   // setLoading(false)
  //     // })
  // }, [])

  // if(!posts) return null
  // const loginPage = (email,password) => {
  // axios.post(baseURL + 'login', {
  //       email,
  //       password
  //     }, {
  //       headers: {
  //         'Authorization': `Basic 12345688797897` 
  //       }
  //     })

  // }
  // return (
  //   <div className="App">
  //     <div className='login-block'>
  //       <LoginForm></LoginForm>
  /* <input value={email} onChange={(e) => {setEmail(e.target.value)}} placeholder='Email'></input>
  <input value={password} onChange={(e) => {setPassword(e.target.value)}} placeholder='Password' type='password'></input>
  <button onClick={() => loginPage(email,password)}> Sign In </button>

  {
    // loading === true ? "Loading ..." : 
    // (errorMessage !== null ? errorMessage : 
    //   posts.map(function(post) {
    //     return (
    //       <div key={post.id}>
    //         {post.id}:  {post.title}
    //       </div>
    //     )
    //   })
    //   )
    posts.map(function(post) {
      return (
        <div key={post.id}>
          {post.id}:  {post.title}
        </div>
      )
    }) 
  } */
  //     </div>
  //   </div>
  // );
}

export default App;
