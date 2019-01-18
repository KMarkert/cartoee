---
title: 'cartoee: Publication quality maps using Earth Engine'
tags:
  - Python
  - Earth Engine
  - Cartopy
  - Matplotlib
authors:
 - name: Kel N Markert
   orcid: 0000-0002-7557-0425
   affiliation: "1, 2"
affiliations:
 - name: Earth System Science Center, The University of Alabama in Huntsville
   index: 1
 - name: SERVIR Science Coordination Office, NASA Marshall Space Flight Center
   index: 2
date: 17 January 2019
bibliography: paper.bib
---

# Summary

Google Earth Engine [@Gorelicketal2017] is a cloud-based geoprocessing platform that provides easy access to petabytes of Earth science and remote sensing datasets that is colocated with computational resources for scientific algorithm development. Access to Earth Engine is provided through a simple application programming interface (API) in JavaScript and Python programming languages. An online development environment is provided for rapid prototyping and visualization using the JavaScript API [@CodeEditor]. Additionally, Earth Engine allows for easy dissemination of algorithms and results through their online code editor and interactive applications backed by Earth Engine's resources, without needing to be an expert in application development, web programming. Although there are great resources to use, visualize, and distribute result from Earth Engine through the web, there are limited pathways for scientists to easily and quickly create publication quality figures using Earth Engine. A typical workflow would require the data be processed on Earth Engine, the data exported to the users local computer, and then the user creates a map or figure.

``Cartoee`` is a Python package that bridges server-side processing of Earth Engine to client-side map creation without having to download data using the Earth Engine Python API. The motivation of ``Cartoee`` is to help scientist create high-quality figures using Earth Engine quickly, in an established library, and with minimal data transfer. The API for ``Cartoee`` was designed for users who are familiar with creating maps in Earth Engine's JavaScript API to create figures using the Matplotlib library [@Hunter] while using Cartopy [@Cartopy] to handle cartographic projections and other map elements. Earth Engine is becoming more and more prevalent in the Earth science community as an analysis tool. With ``Cartoee`` scientist will be able to quickly create high-quality figures for publication without having to transfer large volumes of data. The source code for ``Cartoee`` has been archived to Zenodo with the linked DOI: [@zenodo]


# References
