import reactDom from "react-dom";
import React from 'react'

export class createInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          student_name: '',
          student_Id:null,
          student_marks: null
        };
        this.changeName = this.changeName.bind(this);
        this.changeId = this.changeId.bind(this);
        this.changeMarks = this.changeMarks.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    changeName(event) {
        this.setState({student_name: event.target.value});
    }
    changeId(event) {
        this.setState({student_Id: event.target.value});
    }
    changeMarks(event) {
        this.setState({student_marks: event.target.value});
    }
    
    handleSubmit(){
        fetch('/create', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                Student: this.state.student_name,
                Id:this.state.student_Id,
                Marks:this.state.student_marks
            })
          }); 
    }

    render(){
        return(
            <form onSubmit = {this.handleSubmit}>
                <p>
                    Student Name:
                    <input type="text" value={this.state.value} onChange = {this.changeName}/>
                </p>
                <p>
                    Student ID:
                    <input type="text" value={this.state.value} onChange = {this.changeId}/>
                </p>
                <p>
                    Student Marks:
                    <input type="number" value={this.state.value} onChange = {this.changeMarks}/>
                </p>
                <input type="submit" value="Submit" />
            </form>
        )

    }
}

export default createInput;