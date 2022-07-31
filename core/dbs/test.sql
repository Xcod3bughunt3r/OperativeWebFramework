-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
-- Client :  localhost:8889
-- The MIT License (MIT).
-- Copyright (c) 2022 ALIF-FUSOBAR.
-- -*- coding: utf-8 -*-
-- description:Search log file from website name

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de données :  `testsql`
--

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`) VALUES
(1, 'weidsom', '7b24afc8bc80e548d66c4e7ff72171c5', 'weidsom@thecrackertechnology.com'),
(2, 'sachihenakyy', '7b24afc8bc80e548d66c4e7ff72171c5', 'sachihenakyy@gmail.com');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;