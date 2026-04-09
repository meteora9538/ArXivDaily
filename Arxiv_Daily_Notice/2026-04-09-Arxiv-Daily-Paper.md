# Showing new listings for Thursday, 9 April 2026
Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.


阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送

See `Usage.md` for instructions on how to personalize the repo. 


Keyword list: ['star formation', 'star-forming', 'angular momentum', 'spin', 'disk galaxy', 'fast rotator', 'IMF', 'environment', 'brightest cluster galaxies', 'H alpha emitter']


Excluded: ['gravitational wave']


### Today: 14papers 
#### A Quadruple Excess in Wide Binary Systems: Evidence for Correlated Binary Formation
 - **Authors:** Dolev Bashi, Cathie J. Clarke, Vasily Belokurov
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/2604.06317

 - **Pdf link:** https://arxiv.org/pdf/2604.06317

 - **Abstract**
 Understanding the multiplicity of stellar systems and the correlations between their hierarchical components provides crucial insights into star formation processes. If binary companions form independently in each component of a wide binary (WB), the fraction of quadruple systems, i.e., 2+2 configurations where both components are themselves close binaries (CBs), should equal the product of individual CB fractions. Using \textit{Gaia} DR3 radial velocity spectroscopy (RVS) data for WB systems, we measure the CB fraction $p$ and quadruple fraction $P_{2+2}$, suggesting an enhancement factor $\kappa = P_{2+2}/p^2 = 2.34_{-0.11}^{+0.12}$, significantly exceeding unity expected under a statistical model of independence. We confirm the significance of this excess by performing two sets of tests: (1) shuffling WB pairings while preserving the overall $\Delta G$ distribution shows no significant enhancement, ruling out selection effects; (2) simulations preserving the spectral type (temperature-dependent) CB fraction also yield the same null excess. When examined as a function of WB separation, the enhancement remains strong at separations $\leq 5\,000$ AU, but shows a decline towards unity at the widest separations ($\geq 10\,000$ AU). An independent proper motion anomaly (PMa) consistency check confirms the enhancement, suggesting a similar value. We further find that the enhancement declines with increasing peculiar velocity, suggesting that dynamical processing in older or dynamically hotter populations may transform 2+2 quadruples into triples over time. Our results provide strong evidence for correlated binary formation processes operating in WB systems.
#### Introducing sapphire: Towards Hybrid Physics-Informed, Data-Driven Modeling of Galaxy Formation
 - **Authors:** Viraj Pandya, Greg L. Bryan, T. Lucas Makinen, Austen Gabrielpillai, Christopher Carr, Drummond B. Fielding, Lars Hernquist, Matthew Ho, Kartheik Iyer, Christian Kragh Jespersen, Sophie Koudmani, Marta Laska, Pablo Lemos, Christopher C. Lovell, Lucia A. Perez, William F. Robinson Jr., Rachel S. Somerville, Tjitske K. Starkenburg, Richard Stiskalek, Bryan Terrazas, G. Mark Voit
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2604.06318

 - **Pdf link:** https://arxiv.org/pdf/2604.06318

 - **Abstract**
 Semi-analytic models (SAMs) have been treating galaxy populations as dynamical systems for $\gtrsim50$ years, but their evolution equations remain poorly constrained. We introduce sapphire, a modular, automatically differentiable, GPU-accelerated SAM written from scratch in JAX. For the first time, we compute exact Jacobian matrices of our nonlinear differential equations and show that they have interpretable, non-random structures, using the Pandya et al. (2023) physical model as an initial example. Both local and global sensitivity analyses reveal that supernova energy loading is a key astrophysical parameter for galaxy evolution. We use gradient descent and Hamiltonian Monte Carlo (HMC) to perform comprehensive mock parameter recovery tests. These indicate that the z=0 stellar-to-halo-mass relation alone does not contain enough information to infer many astrophysical parameters. Using observations of star-forming galaxies from the MaNGA survey and the Behroozi et al. (2019) empirical model as one baseline, we derive multiple posteriors assuming different combinations of data, including z=0 interstellar medium gas fractions and metallicities. The inferred physical parameters suggest that galaxies self-regulate their star formation primarily through preventative rather than ejective feedback. Both Fisher and HMC forecasts demonstrate the potential of sapphire to enable precision inference for galaxy formation, but more work is needed to expand its library of models. We discuss how our unique blend of differentiability, massive GPU parallelization, numerical robustness and principled Bayesian methods sets the stage for hybrid physics-informed, data-driven discovery of galaxy formation astrophysics and cosmology. We make sapphire publicly available at this https URL.
#### Binary Star Evolution Modules in REBOUNDx
 - **Authors:** Mohamad Ali-Dib
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR); Earth and Planetary Astrophysics (astro-ph.EP); High Energy Astrophysical Phenomena (astro-ph.HE); Instrumentation and Methods for Astrophysics (astro-ph.IM)
 - **Arxiv link:** https://arxiv.org/abs/2604.06386

 - **Pdf link:** https://arxiv.org/pdf/2604.06386

 - **Abstract**
 Close-binary evolution couples Roche-lobe overflow (RLOF), common-envelope (CE) drag, stellar winds, magnetic braking, and gravitational-wave losses, exchanging mass and angular momentum while reshaping orbits and spins. We present interoperable effects in the REBOUNDx extension to REBOUND that embed these processes within high-accuracy N-body dynamics. The suite includes: a momentum-conserving RLOF operator with conservative and systemic channels and configurable specific-j loss; a CE drag model based on Mach-dependent dynamical friction with kick limiting; isotropic Reimers winds, Parker-type thermal winds, and Eddington-limited outflows powered by a parametric stellar-evolution module supplying mass-dependent R and L; magnetic braking via the Verbunt-Zwaan/Kawaler torque with a saturation-aware closed-form spin update; and post-Newtonian corrections 2PN point-mass and spin-spin; 2.5PN radiation reaction. Linear momentum is conserved for conservative transfer, a minimal corrective torque enforces angular-momentum consistency, and adaptive sub-stepping stabilizes evolution near contact. Inter-module flags coordinate wind/RLOF/CE activity. The unit-agnostic framework enables self-consistent, time-resolved studies of close binaries in isolated or dynamically rich settings. Multiple examples and comparisons against other codes are provided in the Appendix. The code is available at this https URL .
#### The Evolution of Star-Forming Gas in STARFORGE: From Clouds, to Cores, to Stars
 - **Authors:** Ananya Kaalva, Stella S. R. Offner, Nina Filippova, Michael Y. Grudic
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2604.06471

 - **Pdf link:** https://arxiv.org/pdf/2604.06471

 - **Abstract**
 Star formation occurs within dense regions of giant molecular clouds (GMCs), however, exactly how gas collects and evolves to form individual stars and what role dense cores play remains unclear. We use the Lagrangian cell information in the STARFORGE simulation suite to track star-forming gas in three GMCs with varying magnetic field strengths. We find that, once a protostar forms, the lifetime of the unaccreted gas correlates with the final stellar mass, where low-mass stars ($M_*$ < 0.5 M$_\odot$) accrete for 0.5-0.6 Myr from a relatively local reservoir of gas, and high-mass stars ($M_*$ > 2 M$_\odot$) accrete over 3.3-4.7 Myr from a much larger volume. Although the protostellar accretion time increases weakly with magnetic field strength, the accreting gas radii, velocity dispersions, virial parameters, and magnetic energy ratios are largely insensitive to the global cloud properties. At the time of protostar formation, the unaccreted gas exhibits linewidth-size and mass-size relations characteristic of turbulently regulated, isothermal dense cores, following $\sigma_v \propto R^{1.0-1.1}$ and $M \propto R^{0.47-0.55}$, respectively. Low- and intermediate-mass stars undergo relatively continuous accretion and their accretion histories are well-fit by either isothermal sphere, turbulent core, or competitive accretion models, where no one model fits all masses. However, many high-mass stars experience intermittent accretion and their accretion histories are not well-fit by any of these models. While the distribution of accreting gas is more extended than typically-defined dense cores, the physical properties and structure of the star-forming gas resemble those of observed cores and are largely regulated by turbulence and feedback.
#### Data-Driven Constraints on Magnetar Population: No Evidence for a Distinct White Dwarf Channel
 - **Authors:** R. V. Lobato
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/2604.06472

 - **Pdf link:** https://arxiv.org/pdf/2604.06472

 - **Abstract**
 Magnetars are usually interpreted as highly magnetized neutron stars, yet a small subset of low spin-down sources has motivated alternative scenarios involving highly magnetized white dwarfs. We test whether the observed magnetar sample is consistent with a single neutron-star population or whether the data favor an additional compact-object channel. We combine exploratory machine-learning diagnostics with hierarchical Bayesian population modeling. First, we apply principal component analysis and K-means clustering in $(P,\dot{P},L_X)$ space, and then train a Random Forest classifier with leave-one-out cross-validation to identify the observables driving the empirical split. We subsequently construct a hierarchical Bayesian mixture model that links spin parameters to magnetic-field distributions through covariate-dependent mixing fractions. Posterior inference is performed with Hamiltonian Monte Carlo, and predictive performance is assessed with Pareto-smoothed importance sampling leave-one-out cross-validation. The exploratory analysis reveals a reproducible sub-structure: the Random Forest reaches $>95\%$ LOOCV accuracy, with $L_X$, $\dot{P}$, and $kT$ emerging as the dominant predictors. However, the Bayesian comparison shows no statistically significant preference for a two-population model. Instead, a few low spin-down sources receive intermediate posterior membership probabilities, indicating that they are better interpreted as transitional or outlying objects than as members of a clearly distinct class. Overall, current data do not require a separate white-dwarf magnetar population. The main result is therefore conservative but strong: the observed sample is adequately described by a predominantly neutron-star population, while still allowing physically interesting deviations in specific sources.
#### A Close Quasar Pair in a Massive Galaxy Merger at $z=5.7$
 - **Authors:** Minghao Yue, Xiaohui Fan, Anna-Christina Eilers, Feige Wang, Jinyi Yang, Robert A. Simcoe
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2604.06504

 - **Pdf link:** https://arxiv.org/pdf/2604.06504

 - **Abstract**
 Close quasar pairs are rare products of galaxy mergers in which both supermassive black holes (SMBHs) are actively accreting, offering strong constraints on merger-driven active galactic nuclei (AGN) evolution. Identifying close quasar pairs at $z\gtrsim4$ is challenging due to the declining quasar number density in the early Universe. Here we report the confirmation of a close quasar pair at $z=5.7$, J2037--4537, utilizing high-resolution Atacama Large Millimeter/submillimeter Array (ALMA) observations. The quasar host galaxies exhibit tidal disturbed features in both the far-infrared continuum emission and the {\cii} line emission, ruling out the doubly-imaged lensed quasar scenario. The two quasar hosts are massive $(M_\text{dyn}\gtrsim10^{10}M_\odot)$ and star-forming (SFR $\gtrsim500 M_\odot~ \mathrm{yr^{-1}}$). The confirmation of J2037--4537 puts a lower limit on the quasar pair fraction at $5.5<z<6$, $F_\text{pair}>1.2\%$, which is much higher than the quasar pair fraction at $z\lesssim4$. J2037--4537 is expected to form a gravitationally-bound SMBH binary within $\lesssim2$ Gyr. The elevated quasar pair fraction at $z>5.5$, as indicated by J2037--4537, likely contributes to the high gravitational-wave background reported by recent Pulsar Timing Array experiments.
#### The host galaxies and merger environments of short and long gamma-ray bursts producing kilonovae
 - **Authors:** Hannah Skobe, Brendan O'Connor, Antonella Palmese, Lewi Westcott, Christopher J. Conselice, Katelyn Breivik
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/2604.06586

 - **Pdf link:** https://arxiv.org/pdf/2604.06586

 - **Abstract**
 Gamma-ray bursts (GRBs) have traditionally been classified by their prompt emission duration and spectral hardness, with short GRBs (sGRB; $\lesssim2 \ \rm{s}$) originating from compact object mergers and long GRBs (LGRB; $\gtrsim2 \ \rm{s}$) from massive star core-collapse. Recent kilonova (KN) associations with long-duration GRBs have challenged this standard picture. We analyze the host galaxies of nine GRBs with associated kilonova candidates at $z<0.6$, including five sGRB-KNe and four LGRB-KNe. Using both parametric and non-parametric modeling of the host light distributions, we investigate the progenitor environments of these events and test whether their hosts show evidence for recent galaxy interactions that could favor dynamical formation channels or isolated pathways following merger-driven star formation episodes for neutron star binaries. We find that five of the nine hosts display tidal features that show they have likely undergone recent mergers, suggesting that merger-driven, dynamical formation pathways may contribute in some systems. We find no clear morphological distinction between sGRB-KN and LGRB-KN hosts as both populations span a wide range of morphologies, including ellipticals, spirals, and interacting systems with tidal features. Multi-Sérsic modeling of the host light profiles further shows that host-normalized offsets inferred from single-Sérsic fits can be overestimated when the transient is associated with a specific subcomponent of a complex host light profile. These results highlight the importance of decomposing host morphology into physically relevant components when interpreting GRB environments and galactocentric offsets.
#### Plasma Dynamics of Radiative Cooling Accretion Flow in AM Herculis with XRISM
 - **Authors:** Yukikatsu Terada (1) (2), Kaya Mori (3), Takayuki Hayashi (4), Gabriel L. Bridges (3), Manabu Ishida (2), Axel D. Schwope (5), Mariko Kimura (6), Masayoshi Nobukawa (7), David A. H. Buckley (8) (9) (10), Solen Balman (11) (12), Taichi Ichikawa (1), Atsuto Matsumura (13) (2), Mai Takeo (14), Charles J. Hailey (3), Gavin Ramsay (15), Antonio Rodriguez (16), Samantha Walker (3) ((1) Saitama University, (2) ISAS/JAXA, (3) Columbia University, (4) Kyoto University, (5) Leibniz-Institut fur Astrophysik Potsdam, (6) Kanazawa University, (7) Nara University of Education, (8) South African Astronomical Observatory, (9) University of the Free State, (10) University of Cape Town, (11) Istanbul University, (12) Kadir Has University, (13) Tokyo Metropolitan University, (14) Toyama University, (15) Armagh Observatory and Planetarium, (16) California Institute of Technology)
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); High Energy Physics - Experiment (hep-ex)
 - **Arxiv link:** https://arxiv.org/abs/2604.06591

 - **Pdf link:** https://arxiv.org/pdf/2604.06591

 - **Abstract**
 We present XRISM/Resolve high-resolution X-ray spectroscopy of the prototypical magnetic cataclysmic variable AM Herculis. All satellite lines of highly ionized Fe are fully resolved. Lighter element lines (Si, S, Ca) show 2 - 3 eV widths consistent with purely thermal broadening, while the broader 6 - 7 eV Fe lines require additional bulk Doppler broadening. Spin-phase-resolved modulations are clearly detected in the Fe XXV and Fe XXVI lines, with semi-amplitudes of $81.8\pm6$ km s$^{-1}$ and $132.5\pm9$ km s$^{-1}$, and mean velocities of $143.6\pm6$ km s$^{-1}$ and $225.6\pm8$ km s$^{-1}$, respectively. After removing these bulk Doppler shifts, we obtain intrinsic Doppler widths of $5.23_{-0.15}^{+0.16}$ eV for Fe XXV and $6.23_{-0.18}^{+0.19}$ eV for Fe XXVI, directly revealing gradients of bulk velocity and temperature in the cooling-flow plasma. We additionally examined the resonance anisotropy predicted by Terada et al. (1999, 2001): the equivalent widths of the Fe XXV and Fe XXVI resonance lines increase at the pole-on phase by factors of 1.30 - 1.35, in positive correlation with their oscillator strengths. Combining XRISM with simultaneous NuSTAR data and PSAC/MCVSPEC plasma models, we derive a self-consistent shock temperature of $24.0\pm0.1$ keV and shock velocity of $1,116\pm2$ km s$^{-1}$. Radiative transfer simulations of the resonance lines further constrain the shock density to about $(5 - 6)\times10^{15}$ cm$^{-3}$, providing a new density diagnostic for accretion columns. The resulting accretion column geometry has a height of 200 - 300 km and a radius of 200 - 400 km.
#### An Aligned Very-Low-Mass Star Orbiting an M dwarf and Obliquity Patterns Across Giant Planets, Brown Dwarfs, and Binary Stars
 - **Authors:** Tianjun Gan, Alexandrine L'Heureux, Étienne Artigau, Charles Cadieux, René Doyon, Neil J. Cook, Shude Mao
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/2604.06595

 - **Pdf link:** https://arxiv.org/pdf/2604.06595

 - **Abstract**
 Stellar obliquity serves as a key diagnostic for tracing the dynamical evolution of bound systems-from giant planets and brown dwarfs to stellar binaries-revealing whether these diverse populations share analogous histories. Here, we report the first obliquity measurement for a double M dwarf system, determined via the Rossiter-McLaughlin effect. The spin axis of the primary star, TOI-5375 ($M_\ast=0.62\pm0.02\,M_\odot$), is well aligned with the orbit of its low-mass stellar companion ($M_c=84.8\pm1.5\, M_J$, $\rm P=1.72\,days$) with a projected obliquity of $\lambda=-13.5_{-13.8}^{+12.4}\,^{\circ}$ and a true 3D obliquity of $\psi=37.5_{-13.4}^{+10.6}\,^{\circ}$. The result indicates that the system either formed with a primordially aligned configuration or has undergone tidal realignment. We further investigate obliquity patterns across giant planets, brown dwarfs and binary stars. It turns out that a few obliquity trends observed in giant planets also tentatively exhibit in the latter two higher-mass populations: 1) well-aligned orbits are preferentially found around cooler host stars ($T_{\rm eff}\leq 6250\,K$); 2) wide-orbit ($a/R_\ast\geq 10$) companions are predominantly aligned; 3) no significant correlation shows up between obliquity and orbital eccentricity in any of the companion classes. By modeling $|\lambda|$ with a two-component Gaussian distribution, we find that the low-$|\lambda|$ components of binary stars and brown dwarfs are more concentrated near zero than giant planets while the high-$|\lambda|$ components of brown dwarfs and binaries remain unclear due to the small sample size.
#### Habitability Study of Terrestrial Planets: Application to Venus-like Worlds
 - **Authors:** Swathi Raviprakash, Madhu Kashyap Jagadeesh, Margarita Safonova, Oleg Kotsyurbenko
 - **Subjects:** Subjects:
Earth and Planetary Astrophysics (astro-ph.EP)
 - **Arxiv link:** https://arxiv.org/abs/2604.06792

 - **Pdf link:** https://arxiv.org/pdf/2604.06792

 - **Abstract**
 The study of planetary habitability beyond Earth remains a central and challenging project in planetary science. Analysis of large volumes of planetary data from space missions such as CoRoT, Kepler, and JWST is directed ultimately at finding a planet similar to Earth, the Earth's twin, and answering the question of potential exo-habitability. The Earth Similarity Index (ESI) is a first step in this quest, ranging from 1 (Earth) to 0 (totally dissimilar to Earth). To identify planets that may be habitable to the extreme forms of life, we introduce the Mars Similarity Index (MSI). However, extreme forms of life have also been hypothesized under specific conditions in the upper atmosphere of Venus, motivating comparative habitability studies beyond Earth and Mars. The Venus Similarity Index (VSI), introduced here, is defined as the geometric mean of radius, density, escape velocity, and surface temperature, normalized in Venus units (VU). VSI values range from 0 (complete dissimilarity) to 1 (maximum similarity). The VSI provides a comparative framework for identifying Venus-like planetary environments within exoplanet populations. To explore habitability evolution, we further introduce the Ancient Venus Similarity Index (AVSI) and the Future Earth Similarity Index (FESI) to examine early Venusian conditions relative to ancient Earth and to assess potential future evolutionary pathways for Earth-like planets.
#### Magnetic geometry of M dwarfs in the southern PLATO field
 - **Authors:** M. Diez, P. I. Cristofari, J. Morin, P. Petit, S. Bellotti, A. Vidotto, A. Carmona, X. M. Delfosse, C. P. Folsom, G. A. J. Hussain, A. F. Lanza, S. Messina
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/2604.06821

 - **Pdf link:** https://arxiv.org/pdf/2604.06821

 - **Abstract**
 M dwarfs are the most abundant stars in the Galaxy and exhibit diverse magnetic behaviours. Understanding their large-scale magnetic fields is essential to study stellar dynamos and assess the impact of magnetic activity on planetary environments, yet their magnetic properties and long-term variability remain poorly characterised. We aim to characterise the large-scale magnetic fields of 6 M dwarfs in the southern PLATO field, with rotation periods from ~1 to 17 days and masses between 0.26 and 0.64 Msun. Five stars are partially convective, one fully convective, extending the mass-rotation diagram to previously unsampled regions. We analysed TESS light curves to determine accurate rotation periods and optimise phase coverage for spectropolarimetric observations. SPIRou data were reduced to obtain LSD profiles and longitudinal field measurements, while synthetic spectra fitting yielded small-scale field strengths. ZDI was applied to reconstruct large-scale magnetic topologies. We report a wide diversity of magnetic topologies among the 6 M dwarfs, with 3 main results: (1) Rapidly-rotating (Prot < 2 d) early M dwarfs can generate dipole-dominated fields of moderate intensity, similar to less massive mid-M dwarfs; (2) rapidly-rotating mid-M dwarfs can generate non-axisymmetric large-scale fields with a significant toroidal component; (3) a moderately-rotating (Prot ~ 17 d) early M dwarf shows a surprisingly weak large-scale field. Our findings highlight the diversity of magnetic configurations, including in previously unexplored regions. Long-term monitoring is crucial to distinguish persistent features from variability-driven excursions and to characterise the evolution of surface magnetic fields. Complementary PLATO photometry, including flare and spot-induced variability analyses, will be essential to link surface activity with magnetic properties.
#### Magnetic-Field-Induced Inspiral of Binaries with Circumbinary Disk: Black Hole and Protostellar Systems
 - **Authors:** Tomoaki Matsumoto, Kenta Hotokezaka, Kohei Inayoshi
 - **Subjects:** Subjects:
Solar and Stellar Astrophysics (astro-ph.SR); High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/2604.06904

 - **Pdf link:** https://arxiv.org/pdf/2604.06904

 - **Abstract**
 The orbital decay of binary systems is a critical process for understanding the evolution of massive binary black holes (MBBHs) and binary star formation. Performing high-resolution three-dimensional magnetohydrodynamic (MHD) simulations, we investigate a binary system that accretes gas from an infalling envelope analogous to the collapse of molecular clouds in the context of binary star formation. Our simulations reveal the presence of outflows/jets launched from both the circumstellar (mini) disks and the circumbinary disk (CBD). The magneto-rotational instability is also excited within the CBD. These magnetic processes efficiently extract orbital angular momentum from the binary and thus drive orbital decay, while a purely hydrodynamical model exhibits orbital expansion. The decay rate reaches $\sim 0.3-0.7\%$ per orbital period, depending on the initial magnetic field strength. By appropriately scaling these numerical results, we propose a new mechanism for MBBHs mergers within a Hubble time, overcoming the bottlenecks encountered at separations near the final parsec scales. Additionally, we present a formation scenario for close twin binary star systems, emphasizing the significant role of magnetic processes in driving orbital evolution across various astrophysical systems.
#### Metal Mayhem at $\rm z \sim 7-10$: Diversity and Evolution of Gas-Phase Metallicity Gradients
 - **Authors:** Maria Koller, Roberto Maiolino, Hannah Übler, Qiao Duan, Jan Scholtz, Santiago Arribas, William M. Baker, Stefano Carniani, Stephane Charlot, Mirko Curti, Luca Graziani, Gareth Jones, William McClymont, Michele Perna, Bruno Rodríguez Del Pino, Sandro Tacchella, Alessandra Venditti, Giacomo Venturi, Joris Witstok
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2604.07076

 - **Pdf link:** https://arxiv.org/pdf/2604.07076

 - **Abstract**
 We present a JWST/NIRSpec-IFU study of metallicity gradients in seven low-metallicity systems at $z=7.2-9.5$. The main sample spans stellar masses of $\rm \log(M_*/M_{\odot}) \sim 7.8-9.5$, star formation rates (SFRs) of $\rm \log(\text{SFR} / M_{\odot} \text{yr}^{-1}) \sim 0.5-2.5$, and gas-phase metallicities of $4\%-15 \%~Z_\odot$. Within our sample, we also identify three low-metallicity satellite galaxies associated with two of our sources, providing a rare view of early-epoch interactions. The three satellites exhibit even more primordial properties, with metallicity $3\% -4\% ~Z_\odot$ and low star-formation activity ($\rm \log(\text{SFR} / M_{\odot} \text{yr}^{-1}) \sim -0.5$ to $-0.9$). We find that our galaxies, and especially the satellites, are significantly offset from the local Fundamental Metallicity Relation (FMR), with deviations reaching $\Delta \text{FMR} \approx -0.9$ dex. This indicates that these galaxies are likely experiencing strong accretion of pristine gas. Overall, we observe a large scatter in radial metallicity gradients, ranging from positive to negative with an average metallicity gradient of $\rm -0.02 \pm 0.04 \ dex \ kpc^{-1}$. Flat gradients are found in systems with confirmed satellites, suggesting that tidal interactions and mergers drive the radial mixing necessary to homogenise the interstellar medium. The (tentative) presence of an AGN in two of our sources suggests that strong feedback may also be responsible for the observed flat gradients. Conversely, the detection of a positive gradient in one source points toward a direct funnelling of metal-poor gas inflow into the central region of the galaxy. These results show that galaxies in the first billion years grow through diverse, episodic processes, suggesting that early evolution is characterised by structural variety rather than a single, predictable path.
#### Tracing the dynamical and structural complexity of spiral galaxy centres
 - **Authors:** Iris Breda, Glenn van de Ven, Sabine Thater, J. Falcón-Barroso, Prashin Jethwa, Masato Onodera, Joop Schaye, Jarle Brinchmann, Bodo Ziegler, Federica Mauro
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2604.07297

 - **Pdf link:** https://arxiv.org/pdf/2604.07297

 - **Abstract**
 The formation of late-type galaxies has traditionally been described via two pathways: one producing pressure-supported classical bulges, the other rotationally supported pseudo-bulges. Early studies relied on photometric decompositions assuming an exponential disk extrapolated inwards. Recent high-resolution observations, however, reveal a far more complex landscape in disk galaxy centres. We investigated the morphology of central stellar components in intermediate-to-massive spiral galaxies, focusing on disentangling cold, warm, and hot orbital contributions, critically reassessing the standard approach of extrapolating the exponential disk profile inwards. We developed GLANCE (Galactic archaeoLogy via chronochemicAl and dyNamiCal modElling), a tool for photometric, chronochemical, and dynamical galaxy analysis, applied to 8 high-resolution MUSE galaxies to derive stellar population properties and decompose orbits into cold, warm, hot, and counter-rotating (CR) components. We uncovered remarkable structural diversity in the dynamically cold central component: one galaxy displays an exponential profile throughout, while the majority exhibit either a pronounced central drop resembling a doughnut-shaped structure or a compact inner disk significantly steeper than the outer disk. Most galaxies hosting nuclear disks are classifiable as classical bulges - hot, old, red, high bulge-to-total ratio - contrasting with galaxies showing a central cold-component deficit. Beyond the bulge, cold plus warm orbit contributions remain below the total, indicating non-negligible hot or CR orbits with Sérsic indexes consistently above unity. These results highlight the composite nature of disk galaxy centres and the need for decomposition methods that avoid extrapolating the outer disk inwards, requiring large IFS samples across a broad mass range, complemented by simulations such as IllustrisTNG50.


by olozhika (Xing Yuchen). 


2026-04-09
