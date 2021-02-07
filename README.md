<p align="center">

  <h3 align="center">RestfulMarketing</h3>

  <p align="center">
    Marketing API for ConAssist.
    <br />
    <br />
    <a href="https://github.com/Jailoodu/RestfulMarketing/issues">Report Bug</a>
    ·
    <a href="https://github.com/Jailoodu/RestfulMarketing/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

RestfulMarketing is a REST API that allows event organizers to keep track of marketing campaigns. It is part of the ConAssist application, which adheres to the microservices architecture. This project utilizes Google Firestore as the database which stores all of the user data.


### Built With

* [Python]()
* [Flask]()
* [Docker]()
* [Google Firestore]()


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/Jailoodu/RestfulMarketing.git
   ```

<!-- USAGE EXAMPLES -->
## Usage

This project is built upon RESTful architecture, therefore it is ideal if one is familiar with it. The following steps assume that you are running this application locally with the default settings. You can utilize CURL or an application like Postman to submit requests.

1. Run the command.
   ```sh
   python app.py
   ```

2. Head over to http://127.0.0.1:5000/api/, where the Swagger UI is hosted. You will be able to view API definitions and examples of all the available endpoints.

## Testing

[Pytest](https://docs.pytest.org/en/stable/) was utilized to test this repository. The unit tests and acceptance tests can be found in `./tests/test_app.py`, while the 
stress tests can be found in `./tests/test_stress.py`. 

To run the tests, the serviceAccount.json.enc file needs to be decrypted, please message the developers to request the decryption command. Then run the command `python -m pytest --cov=api tests/`.

Travis CI is being utilized to automate testing, you can find the instance [here](https://travis-ci.org/github/Jailoodu/RestfulMarketing).

A static copy of the coverage report is located at `./docs/coverage.png`.


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Jailoodu/RestfulMarketing/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jaison Loodu - jaison_loodu@yahoo.ca

Project Link: [https://github.com/Jailoodu/RestfulMarketing](https://github.com/Jailoodu/RestfulMarketing)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username