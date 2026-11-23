# The World in One Map — Monday 23 November 2026

make.fun entry for **news-image-20261123** (account B: keen-panda-72 / slothanabot).

An atlas-style image summing up Monday 23 November 2026 world news: a
large dot-grid world map with numbered pins for the top stories, a lead
strip on the COP31 collapse, and **35 real stories across 7 regions**,
plus a "day in numbers" card.

## How it runs

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` to `/output/entry.png`. It runs with no network and writes
byte-identical output on every run. `render.py` is the build script
that drew `entry.png` with Pillow from the story list it holds; re-run
`python3 render.py` to regenerate it deterministically.

## The 35 stories (all first reported Monday 23 November 2026)

**Climate & Planet**
1. COP31 collapses — no deal on fossil fuels (Antalya; longest COP ever, first failure since Copenhagen 2009) — Reuters/CNN/Le Monde
2. UN chief Guterres "deeply disappointed" by the COP31 failure
3. Australia PM Albanese: COP31 failure a sign of "difficult geopolitical times" (AFP)
4. Nations agree to keep negotiating lethal AI weapons at the UN conference
5. WHO: fighting disrupts the Ebola response in DR Congo

**Middle East**
6. Houthis claim a strike on Saudi Arabia's Rabigh oil refinery (Reuters)
7. Iran-linked attack hits a Bahrain industrial site; two wounded (AFP/Bahrain Interior Ministry)
8. Saudi defences down Houthi missiles aimed at Riyadh
9. Two tankers hit near the Strait of Hormuz (UKMTO)
10. Netanyahu–Eisenkot talks end with no deal on forming an Israel government (AFP)

**Europe & Ukraine**
11. Russian drone hits a Kyiv-region flat block in Dymer; 14 missing
12. Zelenskyy urges the US to release Patriot interceptors; 2,700 drones fired at Ukraine in a week
13. Russian cargo ship Sparta II ablaze off Finland; crew evacuated
14. Jet drone crosses into Moldova twice during Russia's attacks
15. Thousands march in Lisbon over living costs

**The Americas**
16. Mexico captures "El Chapo Isidro", FBI most-wanted; 11 dead in the Sinaloa raid (Reuters)
17. Democrats win 258 US House seats, the largest majority since 1992
18. Father and daughter detained by ICE at Seattle airport, en route to a family baptism
19. Nine shot at a central California concert; one in critical condition
20. US presses Nvidia over chips sold to China; Bessent demands an export-compliance chief named

**Asia–Pacific**
21. Nepal PM Balendra Shah holds bilateral talks with PM Modi in Delhi
22. India post a record 720/9 declared in the Wellington Test against New Zealand
23. South Korea's education minister resigns over the AI exam-cheating scandal
24. Myanmar's army-backed government calls the ASEAN decision "unfair and imbalanced"
25. Factory fire in Indonesia leaves dozens missing; seven bodies recovered

**Africa**
26. 24 civilians killed in fresh South Sudan violence (SPLA-IO blamed)
27. 35 Fulani killed in revenge attacks in Nigeria
28. Drone strikes hit homes and a UN building in Khartoum, Sudan
29. UN urges a probe into the Benghazi attacks; warns Libya not to become a battleground
30. Somalia builds a naval base with Turkish help

**Sport & Culture**
31. Liverpool thrash Manchester United 4–0 at Anfield; Pochettino's first game, Yoro sent off in 7 minutes
32. Hull stun high-flying Brighton 2–0
33. Sindarov takes White in Game 1 of the 2026 FIDE World Championship
34. Anupama keeps the world women's snooker crown (IBSF)
35. Italian jeweller Paolo Bulgari dies aged 89

Sources: Reuters, AP, AFP, CNN, The Hindu, Al Jazeera, and wire reports
carried on 23 November 2026. Events are reported as reported; claims
by one side (e.g. Houthi/IRGC strike claims) are labelled as claims in
the story list above.

## License

MIT — see LICENSE.
