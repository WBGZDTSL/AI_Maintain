# AI(artificial intelligence) Maintain
<a name="readme-top"> </a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/WBGZDTSL/AI_Maintain">
    <img src="Pic/Readme_image/repair.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AI-MAINTAIN</h3>

  <p align="center">
    An case about  predicting and display parts' life by an interactive website
    <br />
    <a href="https://github.com/WBGZDTSL/AI_Maintain/tree/main/Document"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#background">Background</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Background

[<img alt="Air Conditioner Maintenance" src="Pic/Readme_image/Air Conditioner Maintenance.jpg"/>](https://www.penguincool.com/wp-content/uploads/2018/12/63086869_m.jpg)

The company finds it’s costly to arrange a worker to repair a chiller without knowing which parts are failed inside. The worker will have an issue identifying what parts to bring when scheduling their repair job and is time-consuming to fetch the broken parts twice. Therefore, managers first need to know the usage of parts, and can monitor the remaining life of parts in real time.

Here are the problems we will deal with:
* We need select a model to predict parts' life precisely.
* We need to design a dynamic and interactive web page to meet the needs of managers to monitor the life cycle status of parts in real time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [<img alt="Lifelines" height="35" src="Pic\Readme_image\lifelines.png" width="35"/>][Lifelines-url]
* [<img alt="Dash" height="35" src="Pic\Readme_image\dash-board.png" width="35"/>][Dash-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This project requires basic knowledge of python, and two additional libraries, Lifelines and Dash, need to be installed.


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/WBGZDTSL/AI_Maintain.git
   ```
2. Install packages
   ```pycon
    pip install lifelines
    pip install Dash 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

We completed the prediction of the life of specific parts, and displayed the predicted results on the dynamic web page.

_For more details, please refer to the [Documentation](https://github.com/WBGZDTSL/AI_Maintain/tree/main/Document)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

The business impact of the model is estimated as follows.

**Savings**:
When a part reaches a critical life, we can try to monitor it through the dynamic interactive web page, 
check the life of the part in time, and provide effective suggestions for the exchange of parts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Aaron Wei - [@WBGSUPER](https://twitter.com/WBGSUPER) - bangg.wei@gmail.com

Project Link: [https://github.com/WBGZDTSL/AI_Maintain](https://github.com/WBGZDTSL/AI_Maintain)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

In this project we have cited and referenced the following resources, we would like to express our heartfelt thanks!

* [Air conditioner manufacturer](https://www.asahi.com/ajw/articles/13060517)
* [GitHub Readme Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Lifelines-url]: https://lifelines.readthedocs.io/en/latest/index.html#
[Dash-url]: https://dash.plotly.com/