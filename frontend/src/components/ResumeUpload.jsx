import { useState } from "react";
import api from "../services/api";

function ResumeUpload() {

    const [file, setFile] = useState(null);

    const [profile, setProfile] = useState(null);

    const uploadResume = async () => {

        if (!file) {

            alert("Select Resume");

            return;

        }

        const formData = new FormData();

        formData.append("resume", file);

        try {

            const response = await api.post(
                "/upload-resume",
                formData
            );

            setProfile(response.data);

        }

        catch (error) {

            console.log(error);

            alert("Upload Failed");

        }

    };

    return (

        <div className="container mt-5">

            <h1>

                AI Job Recommendation System

            </h1>

            <br />

            <input

                type="file"

                className="form-control"

                accept=".pdf"

                onChange={(e) =>

                    setFile(

                        e.target.files[0]

                    )

                }

            />

            <button

                className="btn btn-primary mt-3"

                onClick={uploadResume}

            >

                Upload Resume

            </button>

            {

                profile && (

                    <div className="mt-5">

                        <h3>

                            Skills

                        </h3>

                        <ul>

                            {

                                profile.skills.normalized_skills.map(

                                    (skill, index) => (

                                        <li key={index}>

                                            {skill}

                                        </li>

                                    )

                                )

                            }

                        </ul>

                        <h3>

                            Education

                        </h3>

                        <ul>

                            {

                                profile.education.normalized_degrees.map(

                                    (degree, index) => (

                                        <li key={index}>

                                            {degree}

                                        </li>

                                    )

                                )

                            }

                        </ul>

                        <h3>

                            Companies

                        </h3>

                        <ul>

                            {

                                profile.experience.companies.map(

                                    (company, index) => (

                                        <li key={index}>

                                            {company}

                                        </li>

                                    )

                                )

                            }

                        </ul>

                        <h3>

                            Projects

                        </h3>

                        <ul>

                            {

                                profile.projects.projects.map(

                                    (project, index) => (

                                        <li key={index}>

                                            {project}

                                        </li>

                                    )

                                )

                            }

                        </ul>

                    </div>

                )

            }

        </div>

    );

}

export default ResumeUpload;