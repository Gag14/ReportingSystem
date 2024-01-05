import { useState } from 'react';
import uuid from 'react-uuid';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';
import WelcomToHomePge from "../../assets/WelcomToHomePage.svg"
import './homePage.css'
import IconCheck from "../../assets/Icon_check.svg"
import CheckedIcon from "../../assets/checked.svg"
import axios from 'axios';
const HomePage = () => {
    const [reportsData, setReportsData] = useState([
        {
            id: 2,
            checked: false,
            partner: "Betzmark",
            priority: "High",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad"
        },
        {
            id: 1,
            checked: false,
            partner: "Betzmark",
            priority: "High",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad"
        },
    ])
    const [doneArray, setDoneArray] = useState(new Set())
    const [show, setShow] = useState(false);
    const [showModal, setShowModal] = useState(false);
    const [partner, setPartner] = useState(null)
    const [priority, setPriority] = useState(null)
    const [textareaData, setTextareaData] = useState('')
    const [errorData,setErrorData] = useState('')
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const handleShowDone = () => setShowModal(true)
    const handleCloseDone = () => setShowModal(false)
    const setSelectedPartner = (evt) => {
        setPartner(evt.target.value)
    }
    const setSelectedPriority = (evt) => {
        setPriority(evt.target.value)
    }
    const setTextarea = (evt) => {
        setTextareaData(evt)
    }
    function sendInfo() {
        axios.post('https://jsonplaceholder.typicode.com/', {
            firstName: 'Fred',
            lastName: 'Flintstone'
        })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    const addReportData = () => {
        console.log(uuid(),"sss")
        if(textareaData){
            const newReportsData = [{
                id: 111,
                partner,
                checked: false,
                priority,
                description: textareaData
            }, ...reportsData,]
            setReportsData(newReportsData)
            setTextareaData('')
            setPriority(null)
            setPartner(null)
            setErrorData(null)
            handleClose()
        }else{
            setErrorData("This field is required !")
        }
       
    }

    const checkReport = (id) => {
        let idx = reportsData.findIndex(item => item.id === id)
        let dataForId = reportsData[idx]
        dataForId.checked = !dataForId.checked
        setReportsData([...reportsData.splice(0, idx), dataForId, ...reportsData.splice(idx + 1)])
        if (doneArray.has(id)) {
            let arr = new Set(Array.from(doneArray))
            arr.delete(id)
            setDoneArray(arr)
        } else {
            let arr = new Set(Array.from(doneArray))
            arr.add(id)
            setDoneArray(arr)
        }

    }


    const submitChecked = () => {
       
        let arr = Array.from(doneArray)
        console.log(arr,"arr")
        arr.forEach((id) => {
            let dataIx = reportsData.findIndex(el => el.id === id)
            if (dataIx !== -1) {
                setReportsData([...reportsData.splice(0, dataIx), ...reportsData.splice(dataIx + 1)])
            }
        })
        let data = new Set(Array.from(doneArray))
        data.clear()
        setDoneArray(data)
    }
    return (
        <div className="general">
            {/* <div className="home-page__green_top"></div>
            <div className="home-page__green_bottom"></div> */}


            <div className="home-page__">
                <img src={WelcomToHomePge} alt="topImage" />
            </div>

            <div className="add_report" onClick={handleShow} >
                <button className="button" >+</button>
                <div>Add a Report</div>
            </div>
            <div className='homePageContent'>

                <div className='reports'>
                    {
                        doneArray.size > 0 ? <div className='doneReports'>
                            <button onClick={handleShowDone}> Done  ( {doneArray.size} ) </button>
                        </div> : null
                    }

                    {reportsData.map(function (object, i) {
                        return <div key={object.id} className='report'>
                            <div className='report-header'>
                                <div className='left'>
                                    <button className={
                                        !object.priority ? 'blue' :
                                            object.priority === 'High' ? 'red' :
                                                (object.priority === 'Medium' ? 'orange' : 'green')}>
                                        {
                                            object.priority ? object.priority : "Not indicated"
                                        }
                                    </button>
                                    <div>
                                        {object.partner ? object.partner : 'All'}
                                    </div>
                                </div>

                                <img src={object.checked ? CheckedIcon : IconCheck} alt='check' onClick={() => checkReport(object.id)}></img>
                            </div>
                            <div className='report-description'>{object.description}</div>
                        </div>;
                    })}
                </div>

            </div>

            <Modal show={show} onHide={handleClose} id='addModal'>
                <Modal.Header closeButton>
                    <Modal.Title>Report</Modal.Title>
                    <Form.Select value={partner}
                        onChange={e => setSelectedPartner(e)}
                    >
                        <option hidden>Partner</option>
                        <option value="Iqsoft">Iqsoft</option>
                        <option value="GamingArtTec">GamingArtTec</option>
                        <option value="Uru24">Uru24</option>
                        <option value="Gagnat">Gagnat</option>
                        <option value="JazzGroup">JazzGroup</option>
                        <option value="OceanBet">OceanBet</option>
                        <option value="OceanCasino">OceanCasino</option>
                        <option value="SoftVision">SoftVision</option>
                        <option value="Supersiuu">Supersiuu</option>
                        <option value="Woopio">Woopio</option>
                        <option value="BetGames">BetGames</option>
                        <option value="Betzmark">Betzmark</option>
                    </Form.Select>
                    <Form.Select value={priority}
                        onChange={e => setSelectedPriority(e)}>
                        <option hidden>Priorities</option>
                        <option value="Low" className='Low'>Low</option>
                        <option className='Medium' value="Medium">Medium</option>
                        <option className='High' value="High">High</option>
                    </Form.Select>
                </Modal.Header>
                <Modal.Body>
                    <div className='text'>
                        <textarea onChange={(e) => setTextarea(e.target.value)} value={textareaData}></textarea>
                        {
                            errorData ? <div className='red'>{errorData}</div> : null 
                        }
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    <Button className='cancel' onClick={handleClose}>
                        Cancel
                    </Button>
                    <Button className='add' onClick={() => { addReportData() }}>
                        Add
                    </Button>
                </Modal.Footer>
            </Modal>

            <Modal show={showModal} onHide={handleCloseDone}>
                <Modal.Header closeButton >Text</Modal.Header>
                <Modal.Body>
                    <h4>Du iravaci es te martuneci ? </h4>
                </Modal.Body>
                <Modal.Footer>
                    <Button className='cancel' onClick={handleCloseDone}>
                        Cancel
                    </Button>
                    <Button className='submit' onClick={() => { handleCloseDone(); submitChecked(); sendInfo() }}>
                        Submit
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>

    )
}

export default HomePage