// import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
// import Row from 'react-bootstrap/Row';
// import { useState } from 'react';
// import { useNavigate } from "react-router-dom";
// import axios from 'axios';


function PlaintextExample() {
  // const [email, setEmail] = useState('')
  // const [password, setPassword] = useState('')
  // const navigate = useNavigate()
  // const baseURL = 'http://127.0.0.1:5000'
  // function Log_In() {
    
  //   axios.post(baseURL, {
  //     email:email,
  //     password:password
  //   },
  //    ).finally(()=>{
  //     console.log(email.password);
  //    })

  //    {
  //     navigate('/homepage')
  //    }
  //  ;
  // }


  return (
    <Form>
      {/* <h4>SIGN IN</h4>
      <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail" >
        <Form.Label column sm="2">
          Email
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext value={email} onChange={(e) => setEmail(e.target.value)} placeholder='Email' />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Password
        </Form.Label>
        <Col sm="10">
          <Form.Control type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </Col>
      </Form.Group>
      {/* <button onClick={() => navigate('/')}> Sign In</button> */}
        <br/>
   
      {/* <button style={{background:'#A8C25E',width:'100%'}} onClick={()=>Log_In()}>Sing in </button>  */}
    </Form>
  );
}

export default PlaintextExample;