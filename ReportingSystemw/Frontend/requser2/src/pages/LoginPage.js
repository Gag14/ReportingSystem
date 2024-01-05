import React from "react";
import LoginForm from "../components/LoginForm"
import TopImage from "../assets/topImage.svg"
import BottomImage from "../assets/bottomImage.svg"
const LoginPage  = () => {
    return(
        <div className="login-page">
            <div className="login-page__top">
                <img src={TopImage} alt="topImage" />
            </div>
            <div>
                <LoginForm></LoginForm>
            </div>
            <div className="login-page__bottom">
                <img src={BottomImage} alt="bottomImage" />
            </div>
        </div>
    )
}

export default LoginPage