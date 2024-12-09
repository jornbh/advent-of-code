library(Pmetrics)
library(tidyverse)
library(metrica)
setwd("C:/Users/eskil/Desktop/Iodixanol/Iodixanol")



# Last inn data
data <- PM_data$new("Pasientdata.csv")$data

# Oppdater verdiene
data <- data %>%
  mutate(
    dur = if_else(id == 109 & time == 0, 0, dur),
    dose = if_else(id == 109 & time == 0, 810, dose),
    input = if_else(id == 109 & time == 0, 1, input)
  )

# Filtrer, men behold time == 0
data <- data %>%
  filter(!(id == 109 & out > 80 & time != 0))
data <- PM_data$new(data)


# Hent unike ID-er og filtrer ut NA
unique_id <- as.numeric(data$data$id)
unique_id <- unique_id[!is.na(unique_id)] %>% unique()

# Definer antall i modell- og testgrupper
modeling_sample <- as.integer(length(unique_id) * 0.75)
test_sample <- length(unique_id) - modeling_sample

# Tilfeldig utvalg
set.seed(5)
random_id_75 <- sample(unique_id, size = modeling_sample)
random_id_25 <- setdiff(unique_id, random_id_75)

# Filtrer modelldata
filtered_data <- data$data %>%
  filter(id %in% random_id_25)

# Opprett nytt PM_data-objekt fra filtrerte data
validation_data <- PM_data$new(filtered_data)


setwd("C:/Users/eskil/Desktop/Iodixanol/Iodixanol/Results/2-comp/loops/V")

file_number <- 50
sink("C:/Users/eskil/Desktop/Iodixanol/Iodixanol/Results/2-comp/loops/V/outfile.txt")
cat("eskils feilmelding: Hello there\n")

for (i in 1:file_number) {
    # Last inn modellen for filen
    prior_res <- PM_load("C:/Users/eskil/Desktop/Iodixanol/Iodixanol/Results/2-comp/loops/V" + i)  # PM_load skal ta filnummer som argument
    
    # Kjør modell for gjeldende iterasjon
    fit_val <- PM_fit$new(model = prior_res$model, data = validation_data)
    # Generer filnavn
    file_name <- 100 + i
    
  tryCatch({
    fit_val$run(prior = i, cycles = 0, run = file_name, overwrite = TRUE, intern = TRUE)
    
    # Etter hver iterasjon, gå ett nivå opp i mappestrukturen
    setwd("..")  # Går ett nivå opp i mappestrukturen
    
    cat("Iteration", i, "completed successfully.\n")
  }, error = function(e) {
    # Logg feilen og fortsett
    cat("Error in iteration", i, ":", e$message, "\n")
    
    # Etter en feil, gå ett nivå opp i mappestrukturen for å prøve på neste iterasjon
    setwd("..")
  })
}


cat("All iterations completed.\n")