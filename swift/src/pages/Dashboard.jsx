import robot from '../assets/robot.jpg'; // Importing robot image
import logo from '../assets/logo.png'; // Importing logo image
import '../Dashboard.css'; // Importing CSS file
import Bot from '../components/Bot'; // Importing the Bot component
import { useState } from 'react'; // Importing useState hook

const Dashboard = () => {
    const [showBotContent, setShowBotContent] = useState(false); // State to manage visibility of Bot component

    // Function to handle click event for "Experiment now" button
    const handleExperimentClick = () => {
        setShowBotContent(!showBotContent); // Toggling visibility of Bot component
    };

    return (
        <>
            <div className="wrapper">
                <header>
                    <a href="/"><img src={logo} alt="Unit testing Logo"/></a> {/* Rendering logo */}
                    <nav>
                        <ul>
                            <li><a href="/" className="active">Home</a></li>
                            <li><a href="#information">Information</a></li>
                            <li><a href="#OurVision">Our Vision</a></li>
                            <li><a href="https://github.com/iolimat/mena-hack">GITHUB</a></li>
                        </ul>
                    </nav>
                </header>

                <main>
                    <div className="first">
                        <div className="left-col">
                            <h1>TECHTEERRA</h1>
                            <p className="subhead">
                                Effortlessly find datasets, simplify your workflow, and ensure reliability. 
                                Say goodbye to manual searches and hello to efficient data discovery.
                            </p>
                            <div className="cta-btns">
                                <a href="#" className="primary-cta">Documentation</a>
                                
                                <a href="#" className="secondary-cta" onClick={handleExperimentClick}>
                                    <span>Experiment now </span>
                                    <svg viewBox="0 0 19 8" fill="none">
                                        <path d="M18.3536 4.35355C18.5488 4.15829 18.5488 3.84171 18.3536 3.64645L15.1716 0.464466C14.9763 0.269204 14.6597 0.269204 14.4645 0.464466C14.2692 0.659728 14.2692 0.976311 14.4645 1.17157L17.2929 4L14.4645 6.82843C14.2692 7.02369 14.2692 7.34027 14.4645 7.53553C14.6597 7.7308 14.9763 7.7308 15.1716 7.53553L18.3536 4.35355ZM0 4.5H18V3.5H0V4.5Z" fill="white"/>
                                    </svg> 
                                </a>
                            </div>
                        </div>
                        <div className="right-col">
                            <img src={robot} alt="robot" className="right-img"/> {/* Rendering robot image */}
                        </div>
                    </div>

                    <div className="section-two">
                        <div className="information" id="information">
                            <h1>Project Information</h1>
                            <div className="subhead2">
                                <p>TechTeerra is a project driven by the vision of leveraging IT capabilities to gather and process crucial data <strong>from the web</strong>. Inspired by the wisdom of Galileo Galilei, who urged us to {"\""}
                                Measure what is measurable, and make measurable what is not so,{"\""}. This initiative integrates sophisticated data collection tools such as web scraping, speech-to-text, and optical character recognition with cutting-edge IT solutions. By doing so, <strong>it offers a unique approach to collecting, and processing data.</strong> This system not only enhances the efficiency and scope of data-driven projects but also lays the groundwork for groundbreaking discoveries across various sectors, including environmental science and urban planning. Ultimately, the goal of TechTeerra is to empower researchers, businesses, and policymakers with the data they need to make informed decisions that contribute to building a sustainable future.</p>
                                <ul>
                                    <li><strong>Key Components:</strong>
                                        <ul>
                                            <li>Web scraping</li>
                                            <li>Speech-to-text technology</li>
                                            <li>Optical character recognition</li>
                                        </ul>
                                    </li>
                                    <li><strong>Benefits:</strong>
                                        <ul>
                                            <li>Enhanced efficiency and scope of data-driven projects</li>
                                            <li>Facilitation of groundbreaking discoveries</li>
                                            <li>Applicability in sectors from environmental science to urban planning</li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        
                        <div className="ourVision" id="OurVision">
                            <h1>Our Vision</h1>
                            <p>Our vision is to revolutionize artificial intelligence (AI) development by providing an advanced, efficient, and customizable data preparation system. We prioritize data accessibility, democratizing access to high-quality data to unlock AI&apos;s full potential. Our platform offers innovation through customization, catering to the unique needs of each developer. Sustainability is integral to our practices, with a focus on minimizing environmental impact. We aspire to lead in the AI sector by setting standards for excellence and innovation through ongoing research and development. Ultimately, our goal is to advance AI while making a positive impact on society, economy, and the environment, inviting others to join us in redefining the possibilities in AI with dynamic and limitless data solutions.</p>
                        </div>
                    </div>
                    <div className="white-space"></div>
                </main>

                {/* Rendering the Bot component */}
                <Bot showContent={showBotContent} /> 
            </div>
        </>
    );
}

export default Dashboard;
