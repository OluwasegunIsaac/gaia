#install.packages("countrycode")
#install.packages("extrafont")
#install.packages("rnaturalearth")
#install.packages("rnaturalearthdata")

# Load packages -----------------------------------------------------------
library(tidytuesdayR)
library(tidyverse)
library(extrafont)
library(gganimate)
library(rnaturalearth)
library(rnaturalearthdata)
library(sf)


# Load data ---------------------------------------------------------------
global <- read_csv("global_metadata.csv")


world <- ne_countries(scale = "medium", returnclass = "sf")
world_data <- filter(world)

# Plot global distribution of points
p <- ggplot() +
  geom_sf(data = world_data, fill= "#F5F8FA") + 
  geom_point(data = global, mapping=aes(x=Long, y=Lat, size=richness, colour=area)) +
  guides(color = FALSE) +
  scale_size("Fungal OTU richness of the samples", range = c(0.3,8)) +
  labs(title="The Global Soil Mycobiome consortium dataset", subtitle="Visualisation of the Global Soil Mycobiome consortium dataset global soil samples, \ndemonstrating the Fungal mycobiome diversity presence and colour-coded by collection regions.", caption = "Animation rendered by sample collection date") +
  theme(plot.background = element_rect(fill = "#E1E8ED", colour="#E1E8ED"),
        panel.background = element_rect(fill = "#E1E8ED", colour="#E1E8ED"),
        legend.background = element_rect(fill = "#E1E8ED"),
        legend.key = element_rect(fill = "#E1E8ED", colour="#E1E8ED"), 
        legend.text =  element_text(colour = "#657786", size=12, family="Segoe UI"),
        legend.title =  element_text(colour = "#657786", size=12, family="Segoe UI", hjust=0.5),
        plot.title = element_text(colour = "#1DA1F2", size=20, face="bold", hjust = 0.5, family="Segoe UI"),
        plot.subtitle = element_text(colour = "#657786", size=14, hjust = 0.5, family="Segoe UI"),
        plot.caption = element_text(colour = "#657786", size=10, hjust = 0.5, family="Segoe UI"),
        legend.position="bottom",
        plot.margin = unit(c(0.3, 0.3, 0.1, 0.1), "cm"), #top, right, bottom, left
        axis.title= element_blank(),
        axis.text = element_blank(),
        panel.grid.major = element_blank(),
        axis.ticks = element_blank(),
        panel.grid.minor = element_blank())
p
dev.new(width=7,height=11.1,unit="in", noRStudioGD = TRUE)
ggsave(p, filename = "global2.jpg", width=9,height=6,unit="in")

# Convert to animation
anim <- p +
  transition_states(collection_date, transition_length = 4, state_length = 1) +
  enter_fade() +
  exit_fade() + shadow_mark()
anim
animate(anim, nframes = 355, height = 6, width = 9, units = "in", res=150, fps=35)
anim_save("global_anim2.gif", animation = last_animation())
