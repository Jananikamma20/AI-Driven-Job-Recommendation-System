import { useState } from "react";
import api from "../services/api";

function ResumeUpload() {

    const [file, setFile] = useState(null);

    const [profile, setProfile] = useState(null);

    const [jobDescription, setJobDescription] = useState("");

    const [recommendation, setRecommendation] = useState(null);

    const [loading, setLoading] = useState(false);


    // ==========================================
    // Upload Resume
    // ==========================================

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

            setRecommendation(null);

        }

        catch (error) {

            console.log(error);

            alert("Upload Failed");

        }

    };


    // ==========================================
    // Analyze Recommendation
    // ==========================================

    const analyzeRecommendation = async () => {

        if (!profile) {

            alert("Upload your resume first.");

            return;

        }


        if (!jobDescription.trim()) {

            alert("Enter job description.");

            return;

        }


        setLoading(true);


        try {

            const response = await api.post(
                "/analyze-recommendation",
                {

                    user_id: 1,

                    resume: profile,

                    job: {

                        description: jobDescription

                    },

                    resume_file_name:
                        file ? file.name : ""

                }
            );


            console.log("RECOMMENDATION RESPONSE:", response.data);

            setRecommendation(
                response.data
            );

        }

        catch (error) {

            console.log(error);

            alert(
                "Recommendation analysis failed."
            );

        }

        finally {

            setLoading(false);

        }

    };


    return (

        <div className="container mt-5">

            <h1>

                AI Job Recommendation System

            </h1>


            <br />


            {/* =================================
                Resume Upload
            ================================= */}

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


            {/* =================================
                Resume Profile
            ================================= */}

            {

                profile && (

                    <div className="mt-5">

                        <h2>

                            Resume Profile

                        </h2>


                        <h3>

                            Skills

                        </h3>

                        <ul>

                            {

                                profile.skills &&
                                profile.skills.normalized_skills &&
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

                                profile.education &&
                                profile.education.normalized_degrees &&
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

                                profile.experience &&
                                profile.experience.companies &&
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

                                profile.projects &&
                                profile.projects.projects &&
                                profile.projects.projects.map(

                                    (project, index) => (

                                        <li key={index}>

                                            {project}

                                        </li>

                                    )

                                )

                            }

                        </ul>


                        {/* =================================
                            Job Description
                        ================================= */}

                        <h2 className="mt-5">

                            Job Description

                        </h2>


                        <textarea

                            className="form-control"

                            rows="8"

                            placeholder="Paste the job description here..."

                            value={jobDescription}

                            onChange={(e) =>

                                setJobDescription(
                                    e.target.value
                                )

                            }

                        />


                        <button

                            className="btn btn-success mt-3"

                            onClick={
                                analyzeRecommendation
                            }

                            disabled={loading}

                        >

                            {

                                loading

                                    ? "Analyzing..."

                                    : "Analyze Recommendation"

                            }

                        </button>


                    </div>

                )

            }


            {/* =================================
                Recommendation Result
            ================================= */}

            {

                recommendation && (

                    <div className="mt-5">

                        <h2>

                            Recommendation Result

                        </h2>


                        {/* Overall Match */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Overall Match

                            </h4>

                            <h2>

                                {
                                    recommendation.summary
                                        .overall_match
                                }%

                            </h2>

                        </div>


                        {/* ATS */}

                        <div className="card p-3 mb-3">

                            <h4>

                                ATS Score

                            </h4>

                            <h2>

                                {
                                    recommendation.summary
                                        .ats_score
                                }%

                            </h2>

                        </div>


                        {/* Recommendation */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Recommendation

                            </h4>

                            <h3>

                                {
                                    recommendation.summary
                                        .recommendation
                                }

                            </h3>

                        </div>


                        {/* Matched Skills */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Matched Skills

                            </h4>

                            <ul>

                                {

                                    recommendation.data
                                        .matching
                                        .matched_skills
                                        .map(

                                            (skill, index) => (

                                                <li key={index}>

                                                    {skill}

                                                </li>

                                            )

                                        )

                                }

                            </ul>

                        </div>


                        {/* Missing Skills */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Missing Skills

                            </h4>

                            <ul>

                                {

                                    recommendation.data
                                        .matching
                                        .missing_skills
                                        .map(

                                            (skill, index) => (

                                                <li key={index}>

                                                    {skill}

                                                </li>

                                            )

                                        )

                                }

                            </ul>

                        </div>


                        {/* Skill Gap */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Skill Gap

                            </h4>

                            <p>

                                Gap:

                                {" "}

                                {
                                    recommendation.data
                                        .skill_gap
                                        .gap_percentage
                                }%

                            </p>

                        </div>


                        {/* Experience */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Experience

                            </h4>

                            <p>

                                Resume Experience:

                                {" "}

                                {
                                    recommendation.data
                                        .experience
                                        .resume_years
                                }

                                {" "}years

                            </p>

                            <p>

                                Required Experience:

                                {" "}

                                {
                                    recommendation.data
                                        .experience
                                        .job_years
                                }

                                {" "}years

                            </p>

                            <p>

                                Match:

                                {" "}

                                {
                                    recommendation.data
                                        .experience
                                        .experience_match
                                        ? "Yes"
                                        : "No"
                                }

                            </p>

                        </div>


                        {/* Education */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Education

                            </h4>

                            <p>

                                Match:

                                {" "}

                                {
                                    recommendation.data
                                        .education
                                        .education_match
                                        ? "Yes"
                                        : "No"
                                }

                            </p>

                            <p>

                                Score:

                                {" "}

                                {
                                    recommendation.data
                                        .education
                                        .education_score
                                }%

                            </p>

                        </div>


                        {/* Certification */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Certification

                            </h4>

                            <p>

                                Match:

                                {" "}

                                {
                                    recommendation.data
                                        .certification
                                        .certification_match
                                        ? "Yes"
                                        : "No"
                                }

                            </p>

                            <p>

                                Score:

                                {" "}

                                {
                                    recommendation.data
                                        .certification
                                        .certification_score
                                }%

                            </p>

                        </div>


                        {/* Projects */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Projects

                            </h4>

                            <p>

                                Score:

                                {" "}

                                {
                                    recommendation.data
                                        .projects
                                        .project_score
                                }%

                            </p>

                            <ul>

                                {

                                    recommendation.data
                                        .projects
                                        .matched_projects
                                        .map(

                                            (project, index) => (

                                                <li key={index}>

                                                    {project}

                                                </li>

                                            )

                                        )

                                }

                            </ul>

                        </div>


                        {/* Courses */}

                        <div className="card p-3 mb-3">

                            <h4>

                                Recommended Courses

                            </h4>

                            <ul>

                                {

                                    recommendation.data
                                        .recommended_courses
                                        .map(

                                            (course, index) => (

                                                <li key={index}>

                                                    <strong>

                                                        {
                                                            course.course_name
                                                        }

                                                    </strong>

                                                    {" — "}

                                                    {
                                                        course.provider
                                                    }

                                                    {" — "}

                                                    {
                                                        course.level
                                                    }

                                                </li>

                                            )

                                        )

                                }

                            </ul>

                        </div>


                    </div>

                )

            }

        </div>

    );

}


export default ResumeUpload;